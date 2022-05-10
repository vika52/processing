x = 700
def setup():
    size(500,500)
    
def draw():
    global x
    stroke(random(255),random(255),random(255))
    
    #background(200)
    ellipse(250,250,x,x)
    x = x - 1
    if x < 0:
        noLoop()
