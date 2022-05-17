x = 700
angle = 0
angle1 = 0
angle2 = 0
angle3 = 0
def setup():
    size(500,500)
def draw():
    global x,angle,angle1
    stroke(random(255),random(255),random(255))
    translate(50,50)
    push()
    rotate(radians(angle))
    ellipse(5,5,20,20)
    pop()
    rotate(radians(angle1))
    translate(-100,0)
    ellipse(5,5,20,20)
    push()
    translate(-100,0)
    ellipse(5,5,20,20)
    pop()
    push()
    translate(-50,250)
    ellipse(5,5,20,20) 
    pop()
    push()
    translate(-50,350)
    ellipse(5,5,20,20)
    pop()
    push()
    translate(-50,450)
    ellipse(5,5,20,20)
    pop()
    push()
    translate(-50,550)
    ellipse(5,5,20,20)
    pop()
    
    

    
    
    angle = angle + 1
    angle1 = angle1 - 1
    
