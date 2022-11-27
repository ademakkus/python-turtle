import random
import turtle
#global değişkenler
puan=0
#pencere
pencere=turtle.Screen()
pencere.title('Hedef Tıklama Oyunu')
pencere.bgcolor('lightgreen')

#hedef
hedef=turtle.Turtle()
hedef.speed(0)
hedef.shape('circle')
hedef.color('white','red')
hedef.shapesize(3)
hedef.pu()
hedef.goto(0,0,)
#fonksiyonlar
def rastgele_x_y():
    deger=random.randint(-280,280)
    return deger

yazi = turtle.Turtle()
def yazi_olustur(puan):
    yazi.speed(0)
    yazi.shape('square')
    yazi.pu()
    yazi.goto(0, 260)
    yazi.hideturtle()
    if puan==0:
        yazi.write('Başla', align='center', font=('Consolas', 20, 'bold'))
    else:
        yazi.clear()
        yazi.write(f'Puan:{puan}', align='center', font=('Consolas', 20, 'bold'))
def puan_hesapla():
    global puan
    puan=puan+1
    yazi.write(f'Puan:{puan}', align='center', font=('Consolas', 20, 'bold'))
#yazi

#randomx=random.randint(-300,300)
#randomy=random.randint(-300,300)
#hedef.goto(randomx,randomy)
hedef.goto(rastgele_x_y(),rastgele_x_y())
yazi_olustur(puan)
pencere.listen()
def konum_degistir():
    hedef.goto(rastgele_x_y(),rastgele_x_y())
    yazi_olustur(puan)
while True:
    hedef.onclick(konum_degistir)


#enson
turtle.done()