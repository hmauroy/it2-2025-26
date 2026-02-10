class Prikk:
    """Klasse for prikker."""
    canvas = None
    farger = ["chartreuse","yellow","orange","red","magenta","peachpuff","black"]
    """Default klasse for å tegne en ring."""
    def __init__(self,r,x,y):
        self.R = r
        self.x = x
        self.y = y
        self.canvas = Prikk.canvas
        self.tag = "prikk"
        self.fill = "yellow"
        self.outline = ""

    def tegn(self):
        """Tegn prikken i canvas."""
        self.canvas.create_oval(self.x-self.R,self.y-self.R,
        self.x+self.R,self.y+self.R, fill=self.fill, outline=self.outline,
        tags=self.tag)
    
    def __str__(self):
        return f"{self.x},{self.y}"