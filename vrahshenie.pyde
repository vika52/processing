x = 700
angle = 0
angle1 = 0
def setup():
    size(500,500)
    
def draw():
    global x,angle,angle1
    stroke(random(255),random(255),random(255))
    translate(250,250)
    #background(200)
    push()
    rotate(radians(angle))
    ellipse(100,100,20,20)
    pop()
    rotate(radians(angle1))
    ellipse(30,20,30,50)
    angle = angle + 1
    angle1 = angle1 - 1
