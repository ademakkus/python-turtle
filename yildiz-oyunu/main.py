#imports
import random
import turtle
#global değişkenler
renkler=['red','green','blue','yellow','pink','purple','brown','white']

#pencere
pencere=turtle.Screen()
pencere.bgcolor('black')
pencere.setup(800,600)

#
yildiz=turtle.Turtle()
def yildizolustur():
    yildiz.speed(0)
    randomrenk=random.choice(renkler)
    yildiz.color(randomrenk)
    yildiz.pd()
    yildiz.begin_fill()
    boyut=random.randint(25,100)
    for i in range(5):
        yildiz.forward(boyut)
        yildiz.right(144)
    yildiz.end_fill()
    yildiz.pu()
for i in range(10):
    x=random.randint(-300,300)
    y=random.randint(-200,200)
   # yildiz.pu()
    yildiz.setposition(x,y)
   # yildiz.pd()
    yildizolustur()




#en son
turtle.done()