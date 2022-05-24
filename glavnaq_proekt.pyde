x = 700
x1 = 250
y1 = 250
angle = 0
angle1 = 0
angle2 = 0
angle3 = 0
def setup():
    size(500,500)
def draw():
    global x,angle,angle1
    global x1
    global y1
    
    push()
    ellipse(400,150,random(0,100),random(0,100))
    ellipse(50,100,random(0,30),random(0,30))
    pop()
    
    push()
    ellipse(200,150,random(0,100),random(0,100))
    fill(176, 224, 230)
    #ellipse(200,150,100,100)
    pop()
    
    push()
    ellipse(400,400,random(0,50),random(0,50))
    pop()
   
    push()
    ellipse(200,460,random(0,120),random(0,120))
    pop()
    
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


    y1 = y1 + 1
    x1 = x1 +1
    angle = angle + 1
    angle1 = angle1 - 1
