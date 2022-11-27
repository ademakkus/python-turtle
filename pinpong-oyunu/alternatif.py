import turtle
pencere = turtle.Screen()
def pencere_olustur():
    pencere.title('Pin Pong Oyunu -2 ')
    pencere.bgcolor('#3e2723')
    pencere.setup(width=800, height=600)
    pencere.tracer(0)
pencere_olustur()

def raket_olustur(x,y):
    raket_a = turtle.Turtle()
    raket_a.speed(0)
    raket_a.shape('square')
    raket_a.color('white')
    raket_a.penup()
    raket_a.goto(-x, y)
    raket_a.shapesize(5, 1)
raket_olustur(350,1)
raket_olustur(-350,1)

while True:
    pencere.update()

#en son
turtle.done()