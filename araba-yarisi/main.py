#imports
import random
import turtle
import time
#pencere
import winsound
puan: int=100
pencere=turtle.Screen()
canvas=pencere.getcanvas()
root=canvas.winfo_toplevel()

pencere.bgcolor('gray')
pencere.setup(height=700,width=800)
pencere.tracer(0)

pencere.register_shape('racingback.gif')
pencere.register_shape('racingcar.gif')

#yazı
yazi=turtle.Turtle()
yazi.speed(0)
yazi.shape('square')
yazi.color('white')
yazi.pu()
yazi.goto(320,260)
yazi.hideturtle()
yazi.write(f'Puan:{puan}',align='center',font=('Consolas',20,'bold'))
#araba
araba=turtle.Turtle()
araba.speed(0)

araba.speed(0)
araba.shape('racingcar.gif')
araba.shapesize(2)
araba.color('red')
araba.setheading(90)
araba.pu()
#arka plan
arkaplan=turtle.Turtle()
arkaplan.speed(0)
arkaplan.pensize(3)
arkaplan.shape('square')
arkaplan.color('white')
arkaplan.pu()
arkaplan.hideturtle()
arkaplan.goto(0,0)



kamera_dy=0
kamera_y=0

def solagit():
    x=araba.xcor()
    x=x-10
    if x<-170:
        x=-170
    araba.setx(x)
def sagagit():
    x=araba.xcor()
    x=x+10
    if x>170:
        x=170
    araba.setx(x)
engeller=[]
for i in range(10):
    engel=turtle.Turtle()
    engel.speed(0)
    engel.shape('square')
    engel.shapesize(3,6)
    engel.color('red')
    engel.setheading(90)
    engel.pu()
    engel.dx=random.randint(-170,170)
    engel.dy=500
    engel.goto(engel.dx,engel.dy)
    engeller.append(engel)




pencere.listen()
pencere.onkeypress(solagit,'Left')
pencere.onkeypress(sagagit,'Right')
baslangic_zamani=time.time()
i=-1

def kapat():
    global devam
    devam=False
devam=True
while devam:
    #time.sleep(0.001)
    kamera_dy=-2
    kamera_y=kamera_y+kamera_dy
    kamera_y=kamera_y%700

    arkaplan.goto(0,kamera_y-700)
    arkaplan.shape('racingback.gif')
    arkaplan.stamp()
    araba.shape('racingcar.gif')
    araba.stamp()
    #
    arkaplan.goto(0,kamera_y)
    arkaplan.shape('racingback.gif')
    arkaplan.stamp()
    araba.shape('racingcar.gif')
    araba.stamp()
    if time.time()-baslangic_zamani>random.randint(3,6):
        baslangic_zamani=time.time()
        i=i+1
        if i==9:
            i=-1
            for engel in engeller:
               engel.dx = random.randint(-170, 170)
               engel.dy = 500
               engel.goto(engel.dx, engel.dy)
    y=engeller[i].ycor()
    y=y-2
    engeller[i].sety(y)

    if engeller[i].distance(araba)<30:
        winsound.PlaySound('patlama.wav',winsound.SND_ASYNC)
        puan=puan-1
        if puan==0:
            puan=100
            yazi.write(f'Puan:{puan}', align='center', font=('Consolas', 20, 'bold'))
        yazi.clear()
        yazi.write(f'Puan:{puan}', align='center', font=('Consolas', 20, 'bold'))
    pencere.update()
    arkaplan.clear()
    araba.clear()


