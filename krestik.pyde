y1 = 250
x1 = 250
y2 = 250
x2 = 250
y3 = 250
x3 = 250
x4 = 250
y4 = 250
def setup():
    size(500,500)
    
def draw():
    #background(100)
    global y1
    global x1
    global x2
    global y2
    global x3
    global y3
    global x4
    global y4
    fill(random(255),random(255),random(255))
    #strokeWeight(random(50))
    razmer = random(5,50)
    stroke(random(255),random(255),random(255),random(255))
    ellipse(x1,y1,razmer,razmer)
    ellipse(x2,y2,razmer,razmer)
    ellipse(x3,y3,razmer,razmer)
    ellipse(x4,y4,razmer,razmer)
    y1 = y1 + 1
    x1 = x1 + 1
    y2 = y2 + 1
    x2 = x2 - 1
    x3 = x3 + 1
    y3 = y3 - 1
    x4 = x4 - 1
    y4 = y4 - 1
