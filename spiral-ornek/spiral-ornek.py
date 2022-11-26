import turtle
import random as rnd
def kare(a):
    ok.forward(a)
    ok.left(90)
renkler=['red','blue','brown','black','purple','orange','crimson']
ok=turtle.Turtle()
ok.speed(0)
kenar=10
ok.pensize(2)
for i in range(40):
    ok.color(rnd.choice(renkler))
    kare(kenar)
    kenar=kenar+10
    ok.right(10)

turtle.done()