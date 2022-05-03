def setup():
  size(500,500)
  background(0)


def draw():
  #translate(350,350)
  stroke(random(0,255),random(0,255),random(0,255))
  strokeWeight(random(1,150))
  point(random(0,500),random(0,500))
  frameRate(100)
