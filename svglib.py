def header():
    return("<svg xmlns=\"http://www.w3.org/2000/svg\">")

def footer():
    return ("</svg>")

def line(x1,y1,x2,y2,stroke = "black",width = 1):
    return("<line x1=\"" + str(x1) + "\" y1=\"" + str(y1) + "\" x2=\"" + str(x2) + "\" y2=\"" + str(y2) + "\" stroke=\"" + stroke + "\" stroke-width=\"" + str(width) + "\"/>")
        
def circle(cx,cy,r,stroke = "black", width = 1, fill = "white"):
    return("<circle cx=\"" + str(cx) + "\" cy=\"" + str(cy) + "\" r=\"" + str(r) + "\" stroke=\"" + stroke + "\"stroke-width=\"" + str(width) + "\" fill=\"" + fill + "\"/>")

def polyline(fill,stroke,width,points):
    str1 = ' '.join(str(number) for number in points)
    return("<polyline fill=\"" + fill +"\" stroke=\"" + stroke +"\" stroke-width=\"" + str(width) + "\" points=\"" + str1 + "\"/>")
 
