import random
import turtle

# pencre
import winsound
atesler=[]
pencere = turtle.Screen()
pencere.bgcolor('black')
pencere.title('Uzay Savaşı')
pencere.bgpic('uzay.gif')
pencere.setup(width=600, height=600)

turtle.register_shape('oyuncu.gif')
turtle.register_shape('dusman.gif')
turtle.register_shape('ates.gif')
# oyuncu
oyuncu = turtle.Turtle()
oyuncu.color('blue')
oyuncu.speed(0)
oyuncu.shape('oyuncu.gif')
oyuncu.setheading(90)
oyuncu.pu()
oyuncu.goto(0, -250)
oyuncuhizi = 20
ates = turtle.Turtle()
# ateş

ates.color('yellow')
ates.speed(0)
ates.shape('ates.gif')
ates.setheading(90)
ates.pu()
ates.goto(0, -240)
ates.hideturtle()
ates.turtlesize(1, 1)
ateshizi = 20

ateskontrol = True

yazi=turtle.Turtle()
yazi.color('white')
yazi.speed(0)
yazi.pu()
yazi.goto(0,200)
yazi.hideturtle()

def sola_git():
    x = oyuncu.xcor()
    x = x - oyuncuhizi
    if x < -300:
        x = -300
    oyuncu.setx(x)


def saga_git():
    x = oyuncu.xcor()
    x = x + oyuncuhizi
    if x > 300:
        x = 300
    oyuncu.setx(x)
def yukari_git():
    y = oyuncu.ycor()
    y = y + oyuncuhizi
    if y > 270:
        y = 270
    oyuncu.sety(y)
def asagi_git():
    y = oyuncu.ycor()
    y = y -oyuncuhizi
    if y <-270:
        y = -270
    oyuncu.sety(y)


def atesle():
    global ateskontrol
    winsound.PlaySound('lazer.wav',winsound.SND_ASYNC)
    x = oyuncu.xcor()
    y = oyuncu.ycor() + 20
    ates.goto(x, y)
    ates.showturtle()

    global ateskontrol
    ateskontrol = True



hedefler = []
for i in range(8):
    hedefler.append(turtle.Turtle())

for hedef in hedefler:
    hedef.color()
    hedef.speed(0)
    hedef.color('red')
    hedef.turtlesize(1, 1)
    hedef.shape('dusman.gif')
    hedef.pu()
    hedef.setheading(90)
    x = random.randint(-280, 280)
    y = random.randint(180, 260)
    hedef.goto(x,y)

pencere.listen()
pencere.onkey(sola_git, 'Left')
pencere.onkey(saga_git, 'Right')
pencere.onkey(atesle, 'space')
pencere.onkey(yukari_git, 'Up')
pencere.onkey(asagi_git, 'Down')


# ateş et
def ateset():
    y = ates.ycor()
    y = y + ateshizi
    ates.sety(y)


while True:
    if ateskontrol:
        ateset()
    for hedef in hedefler:
        y=hedef.ycor()
        y=y-2
        hedef.sety(y)
        if hedef.distance(ates)<20:
            ates.hideturtle()
            hedef.hideturtle()
            hedefler.pop(hedefler.index(hedef))
            winsound.PlaySound('patlama.wav',winsound.SND_ASYNC)
    if hedef.ycor()<-270 or hedef.distance(ates)<20:
        yazi.write('Oyun bitti! Kaybettiniz.', align='center', font=('Consolas', 20, 'bold'))
    if len(hedefler)==0:
        yazi.write('Tebrikler ! Kazandınız.',align='center',font=('Consolas',20,'bold'))
turtle.done()
