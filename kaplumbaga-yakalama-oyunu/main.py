#import
import turtle
import random as rnd
#global değikenler
renkler=['red','green','blue','orange','brown','teal','purple','indigo']
hedefler=[]
#pencere
pencere=turtle.Screen()
pencere.screensize(800,800)
#pencere.screensize(canvwidth=1000,canvheight=1000)
pencere.title('Kaplumbağa Yakalama Oyunu')
pencere.bgcolor('blue')
pencere.bgpic('light.gif')
pencere.tracer(2)
#oyuncu
oyuncu=turtle.Turtle()
oyuncu.color('white')
oyuncu.shape('triangle')
oyuncu.shapesize(3)
oyuncu.penup() #oyuncu.pu() oyuncu.up() olabilir. hareket ederken çizgi çizme

speed=1
oyuncu.speed(speed)
#sola döndürme fonksiyonu
def solaDon():
    oyuncu.left(90)
def sagaDon():
    oyuncu.right(90)
def hizArtir():
    global speed
    speed=speed+1

def hizAzalt():
    global speed
    speed=speed-1
#
score=0
yaziPuan = turtle.Turtle()
def puanYazdir(score):


    yaziPuan.speed(0)
    yaziPuan.shape('square')
    yaziPuan.color('white')
    yaziPuan.pu()
    yaziPuan.hideturtle()  # kareyi gizle

    yaziPuan.goto((-200, 250))
    yaziPuan.clear()
    yaziPuan.write(f'Puan : {score}', align='center', font=('Courier', 20, 'bold'))

puanYazdir(score)
#klavye kontrolü
pencere.listen() #yazılmalı
pencere.onkey(solaDon,'Left')
pencere.onkey(sagaDon,'Right')
pencere.onkey(hizArtir,'Up')
pencere.onkey(hizAzalt,'Down')
#hedef
def hedefOlustur(maxHedef):
    global hedefler
    for i in range(maxHedef):
        hdf=turtle.Turtle()
        hdf.penup()
        hdf.color(rnd.choice(renkler))
        hdf.speed(0)
        hdf.shape('turtle')
        hdf.setposition(rnd.randint(-300, 300), rnd.randint(-300, 300))
        hedefler.append(hdf)

maxHedef=5
hedefOlustur(maxHedef)

hedef=turtle.Turtle()
hedef.pu()#hedef.penup() hedef.up() olabilir. hareket ederken çizgi çizme
hedef.color('#80d8ff')
hedef.shape('turtle')
hedef.shapesize(2)
hedef.speed(0)
hedef.setposition(rnd.randint(-300,300),rnd.randint(-300,300))

while True:
    oyuncu.forward(speed)
    if oyuncu.xcor()>300 or oyuncu.xcor()<-300:
        oyuncu.right(180)
    if oyuncu.ycor()>300 or oyuncu.ycor()<-300:
        oyuncu.left(-180)
    hedef.forward(1)

    for i in range(maxHedef):
        hedefler[i].forward(5)
        if hedefler[i].xcor()>400 or hedefler[i].xcor()<-400:
            hedefler[i].right(rnd.randint(150,250))
            hedefler[i].color(rnd.choice(renkler))
        if hedefler[i].ycor()>400 or hedefler[i].ycor()<-400:
            hedefler[i].right(rnd.randint(150, 250))
            hedefler[i].color(rnd.choice(renkler))

        if oyuncu.distance(hedefler[i]) < 40:
            hedefler[i].setposition(rnd.randint(-300, 300), rnd.randint(-300, 300))
            hedefler[i].color(rnd.choice(renkler))
            hedefler[i].right(rnd.randint(0,360))
            score=score+1

            puanYazdir(score)

turtle.done()
