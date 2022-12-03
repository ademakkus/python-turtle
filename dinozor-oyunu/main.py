import random
import time
import turtle
puan=100
pencere=turtle.Screen()

canvas=pencere.getcanvas()
root=canvas.winfo_toplevel()

pencere.title('Dinazor Oyunu')
pencere.bgcolor('black')
pencere.setup(width=700,height=650)
pencere.bgpic('back.gif')
pencere.tracer(0)
pencere.register_shape('dino.gif')
pencere.register_shape('cactus.gif')

#dinozor
dinozor=turtle.Turtle()
dinozor.speed(0)
dinozor.shape('dino.gif')
dinozor.pu()
dinozor.dy=0
dinozor.durum='hazir'
dinozor.goto(-200,-50)
yercekimi=-0.5

#kaktus
kaktus=turtle.Turtle()
kaktus.speed(0)
kaktus.shape('cactus.gif')
kaktus.color('red')
kaktus.pu()
kaktus.dx=-5
kaktus.goto(200,-70)

#yazi
yazi=turtle.Turtle()
yazi.pu()
yazi.goto(250,260)
yazi.shape('square')
yazi.color('white')
yazi.speed(0)
yazi.pu()
yazi.hideturtle()
yazi.write(f'Puan:{puan} ', align='center',font=('Consolas',20,'bold'))

def kapat():
    global devam
    devam=False
def atla():
    if dinozor.durum=='hazir':
        dinozor.dy=12
    dinozor.durum='zipliyor'

pencere.listen()
pencere.onkeypress(atla,'space')
root.protocol('WM_DELETE_WINDOW',kapat)
devam=True
while devam:
    time.sleep(0.01)
    if dinozor.ycor()<-50:
        dinozor.sety(-50)
        dinozor.dy=0
        dinozor.durum='hazir'
    if dinozor.ycor()!=-50 and dinozor.durum=='zipliyor':
        dinozor.dy=dinozor.dy+yercekimi
    y=dinozor.ycor()
    y=y+dinozor.dy
    dinozor.sety(y)
    pencere.update()

    x=kaktus.xcor()
    x=x+kaktus.dx
    kaktus.setx(x)
    if kaktus.xcor()<-400:
        x=random.randint(400,600)
        kaktus.setx(x)
        kaktus.dx=kaktus.dx*1.05
    if kaktus.distance(dinozor)<30:
        puan=puan-1
    yazi.clear()
    yazi.write(f'Puan:{puan} ', align='center', font=('Consolas', 20, 'bold'))


