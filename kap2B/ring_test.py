class Ring:
    """Klasse for ringer."""
    canvas = None
    farger = ["chartreuse","yellow","orange","red","magenta","peachpuff","black"]
    """Default klasse for å tegne en ring."""
    def __init__(self,r,x,y):
        self.R = r
        self.x = x
        self.y = y
        self.canvas = Ring.canvas
        self.tag = "ring"
        self.outline = "white"

    def tegn(self):
        """Tegn ringen i canvas."""
        self.canvas.create_oval(self.x-self.R,self.y-self.R,
        self.x+self.R,self.y+self.R, outline=self.outline,tags=self.tag)