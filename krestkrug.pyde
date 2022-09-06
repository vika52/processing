Y1 = 250
y = 250
x1 = 250
X = 250

def setup():
    size(500,500)
def draw():
    global X,y,x1,Y1
    background(0)
    ellipse (x1,250,40,40)
    ellipse (250,y,40,40)
    ellipse (X,250,40,40)
    ellipse (250,Y1,40,40)
    X = X - 1
    x1 = x1 + 1
    y = y + 1
    Y1 = Y1 -1
