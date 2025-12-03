"""
Polarplotter versjon 2.

1) Beregne linjen mellom to punkter ved å finne stigningstall og konstantledd.
2) Bruk funksjonen til å beregne f.eks. 100 punkter langs linjen.
3) For hvert punkt så beregnes lengden av vektorene fra motorer til tegnehodet enkelt.
4) Finn hvor langt motor må bevege seg for å komme til ny lengde.
5) Beregn farten de to motorene må ha for å komme frem til nytt punkt samtidig.
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

    def calc_line(self,x_target, y_target,n_points):
        """
        Find slope and constant from the current point to next.
        Ettpunktsformelen gir denne likningen
        y = a*x - a*x_target + y_target
        y = a*x + b => b = -a*x_target + y_target
        a=3
        P = (4,1)
        b = -3*4 + 1 = -11
        a=5
        P = (2,5)
        b = -5*2 + 5 = -5
        """
        # Figure out if the line is vertical. Then the steps is just n steps along the y-axis.
        if x_target == self.x:
            print("Line along y-axis")
        elif y_target == self.y:
            print("Line along x-axis")
        else:
            a = (y_target - self.y) / (x_target - self.x)
            b = -a*x_target + y_target

        # Find vector distance for movement.
        x_len = x_target - self.x
        y_len = y_target - self.y
        # Divide length by n_points to get step length
        dx = x_len/n_points
        dy = y_len/n_points

        current_point = [self.x,self.y]
        points = [current_point]
        for i in range(n_points):
            current_point = [current_point[0] + dx, current_point[1] + dy]
            points.append(current_point)
        return points


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

x_start = 100
y_start = 200
penn = Penn(5, x_start, y_start, canvas_width)
     


isRunning = True
last_time = time.time()
fps = 3
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
        points = penn.calc_line(x_target, y_target,5)
        print(points)
        for point in points:
            canvas.after(dt)  # venter i x ms.
            canvas.create_oval(point[0],point[1],point[0]+15,point[1]+15, fill="white", tags="point")
            canvas.update()
        #exit()
        #motorRunning = True
        teller += 1
        if teller >= len(targets):
            isRunning = False
        
    
    """
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
    """


# Kjører vinduet. Må være nederst i koden.
window.mainloop()

