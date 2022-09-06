x = 470
x1 = 470
x2 = 470
def setup():
    size(500,500)
    
def draw():
    global x,x1,x2

    background(0)   
    
    ellipse(x,30,40,40)
    ellipse(x,470,40,40)
    ellipse(x,250,40,40)
    x = x - 1
    x1 = x1 - 1
    x2 = x2 - 1
