import math
import svglib

class turtle:
    def __init__(self):
        self.cx = 100
        self.cy = 100
        self.angle = 0
        self.lines = []

    def forward(self,length):
        newx = math.cos(math.radians(self.angle))*length + self.cx
        newy = math.sin(math.radians(self.angle))*length + self.cy
        self.lines.append((self.cx, self.cy,newx,newy))
        
        self.cx = newx
        self.cy = newy

    def back(self,length):
        forward(self,-length)
    def right(self,angle):
        self.angle += angle
    def left(self,angle):
        self.angle += (360-angle)

    def save(self,fileName):
        file = open (fileName + ".svg", "w")
        file.write(svglib.header())

        for x1,y1,x2,y2 in self.lines:
            file.write(svglib.line(x1,y1,x2,y2))
        
        file.write(svglib.footer())
        file.close()
