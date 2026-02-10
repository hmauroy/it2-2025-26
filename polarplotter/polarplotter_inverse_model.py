"""
Simulering av hvordan tegningen blir hvis utgangspunktet for bevegelse av tegnehodet
er lengden på snorene.
Resultatet:
- ser ut som at vannrette streker blir merkbart buet på midten.
- Loddrette streker er ikke like buet på midten, men de har en tendens.
- Loddrette streker vil tegnes med ulik fart langs streken pga konstant fart for motorene.
    Når trådene får mer og mer grunn vinkel vil tegnehodet løftes raskere og raskere.
F.eks. et rektangel ser ut som et typisk tegnet flagg som vaier i vinden.

For hvert punkt så utføres beregningene:
Calculates the speed of the motors.
        Each motor should have equal travel time. 
        1) Find distance for motors and which direction: spool inwards or outwards.
        2) Set longest distance to use v_max.
        3) Calculate time for longest travel distance.
        4) Calculate speed for the shortest travel distance.

Bevegelsen deles opp i n_steps
For hvert steg av den simulerte bevegelsen beregnes det hvor tegnehodet er.
Punkt 2) nedenfor involverer andregrads-likningssett med to ukjente numerisk. Dette er ikke optimalt pga:
    a) Krever mye prosessering.
    b) Er unøyaktig pga numerisk.
    c) Løsning er ikke sikkert man finner pga. man setter initialbetingelser.

1) Move shorten/elongate a_len and b_len in accordance to the speeds or step_length
2) Calculate (x,y) positions using the lengths of the ropes (vectors)

3) draw the point

"""

import tkinter as tk
import time
import numpy as np
from numpy.linalg import norm
from scipy.optimize import fsolve

window = tk.Tk()
window.lift()
window.focus_force()
bredde = 600
hoyde = 600
window.minsize(bredde,hoyde)
window.configure(background="#334467")

# Setter inn en ramme (Frame)
topp_color = "#dddddd"
topp_hoyde = 100
topp = tk.Frame(window,background=topp_color)
topp.configure(
    height=topp_hoyde,
    width=bredde*0.75,
)
topp.pack_propagate(False) # Skrur av at children kan endre rammen.

topp.pack()

# Lager noe tekst med Label
tekst = tk.Label(topp)
tekst["text"] = "Polarplotter"
tekst.configure(
    font = ("Aptos", 30),
    foreground="black",
    background=topp_color
)
tekst.pack()

# 2) Lager en ramme som canvas kan ligge inni
canvas_width = bredde
canvas_height = hoyde - topp_hoyde
canvas_frame = tk.Frame(window)
canvas_frame.pack()

canvas = tk.Canvas(canvas_frame, width=canvas_width,
                   height=canvas_height, background="black")
canvas.pack()

class Motor:
    def __init__(self):
        pass

class Penn:
    def __init__(self,R,x,y,L):
        self.R = R
        self.x = x
        self.y = y
        self.L = L
        self.a = 0
        self.b = 0
        self.ta = 10 # time for movement from point A to point B.
        self.tb = 0
        self.va = 0 # speed of the rope for motor A = speed of the length of vector a.
        self.vb = 0
        self.dr_a = 0
        self.dr_b = 0
        self.dir_a = 1
        self.dir_b = 1
        self.v_max = 10
        self.update_vectors(x,y)
        self.a_len = self.calc_vector_length(self.a)
        self.b_len = self.calc_vector_length(self.b)
        self.isAtTarget = False
        self.n_steps = 15
    
    def update_vectors(self,x,y):
        self.x = x
        self.y = y
        self.a = np.array([self.x,self.y])
        self.b = np.array([self.x-self.L,self.y])
    

    def calc_vector_length(self,v):
        len_v =  norm(v)
        return len_v
    
    def get_lengths(self):
        return f" a_len = {self.a_len}, b_len = {self.b_len} "

    def calc_speeds(self,x2,y2):
        """
        Calculates the speed of the motors.
        Each motor should have equal travel time. 
        1) Find distance for motors and which direction: spool inwards or outwards.
        2) Set longest distance to use v_max.
        3) Calculate time for longest travel distance.
        4) Calculate speed for the shortest travel distance.
        """
        next_point = np.array([x2,y2])
        L_vec = np.array([self.L,0])
        # 1) Find distances of the new vectors pointing to the new point.
        self.dr_a = norm(next_point) - norm(self.a)
        self.dr_b = norm(next_point-L_vec) - norm(self.b)
        #print(f"dr_a = {self.dr_a}, dr_b = {self.dr_b}")
        # Sets directions of spooling: 1 is outwards, -1 is inwards.
        self.dir_a = 1
        self.dir_b = 1
        # Determine if the new distances are longer/shorter
        if self.dr_a < 0:
            self.dir_a = -1
        if self.dr_b <0:
            self.dir_b = -1
        # Check if new distance is longer or shorter
        if abs(self.dr_a) > abs(self.dr_b):
            self.va = self.dir_a * 10
            #print(f"va={self.va}")
            self.ta = abs(self.dr_a) / abs(self.va)
            #print(f"ta={self.ta}")
            self.vb = self.dir_b * abs(self.dr_b) / abs(self.ta)
            self.tb = self.ta   # The travel time is equal.
        else:
            self.vb = self.dir_b * 10
            #print(f"vb={self.vb}")
            self.tb = abs(self.dr_b) / abs(self.vb)
            #print(f"tb={self.tb}")
            self.va = self.dir_a * abs(self.dr_a) / abs(self.vb)
            self.ta = self.tb
        # Update the vectors for the new point
        #print(f"v_a = {self.va}, t_a = {self.ta}, v_b = {self.vb}, t_b = {self.tb}")

    
    def equations(self,vars):
        x,y = vars
        a = self.a_len
        b= self.b_len
        L = 600
        eq1 = x**2 + y**2 - a**2
        eq2 = (L-x)**2 + y**2 - b**2
        return [eq1, eq2]

    def step_motors(self, n_steps):
        """
        1) Move shorten/elongate a_len and b_len in accordance to the speeds or step_length
        2) Calculate (x,y) positions using the lengths of the ropes (vectors)
        3) draw the point
        """
        # 1)
        self.a_len += self.dr_a/n_steps
        self.b_len += self.dr_b/n_steps
        #print(self.get_lengths())
        # 2)
        # Solve x and y coordinates from the length of the vectors using numerical algorithm.
        # Initial guess for the x and y coordinates. They should be close to the current location.
        initial_guess = [self.x,self.y]
        x,y = fsolve(self.equations, initial_guess)
        #print(f"x = {x:.3f}, y={y:.3f}")
        # Updates the vectors and a_len and b_len are calculated again.
        self.update_vectors(x,y)
        

    def tegn(self,canvas):
        R = self.R
        canvas.create_oval(
            self.x-R, self.y-R,
            self.x+R, self.y+R,
            fill="white",
            tags="penn")
    
    def fjern(self,canvas):
        canvas.delete("penn")

x_start = bredde/2
y_start = 400
penn = Penn(5, x_start, y_start, canvas_width)
     


isRunning = True
last_time = time.time()
fps = 50
dt = int(1000/fps)

motorRunning = False
n_steps = 15  # divide movement in 15 points
penn.tegn(canvas)
dr_a = 1
dr_b = 1

x_target = 400
y_target = 400
targets2 = [
    [200,267],
    [250,300],
    [300,333],
    [400,400],
    [366,300],
    [350,250],
    [333,200],
    [300,100],
    [283,48]

]
targets3 = [
    [500,400],
]
targets = [
    [100,400],
    [400,400],
    [400,200],
    [100,200],
]

targets = [
    [bredde/2,400],
    [bredde/2,10],
]

targets = [
    [200,267],
    [400,400],
    [283,48]

]


teller = 0

while isRunning:
    """
    1) Calculate motor speeds
    2) Move motors in steps corresponding to the speeds
    """
    if motorRunning == False:
        next_point = targets[teller]
        x_target = next_point[0]
        y_target = next_point[1]
        print(f"next point: ({x_target},{y_target})")
        penn.calc_speeds(x_target,y_target)
        motorRunning = True
        teller += 1
    else:
        penn.tegn(canvas)
        canvas.after(dt)  # venter i x ms.
        canvas.update()
        #penn.fjern(canvas)
        # Update vector lengths
        penn.step_motors(n_steps)
        if norm( penn.a - np.array([x_target,y_target]) ) <= 1:
            motorRunning = False
            if teller == len(targets):
                # Finished with all points to be drawn.
                print(f"Finished drawing all target points!")
                isRunning = False
                canvas.update()



# Kjører vinduet. Må være nederst i koden.
window.mainloop()

