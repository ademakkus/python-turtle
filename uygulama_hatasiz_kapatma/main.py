import random
import turtle

# pencere
#1. önce pencere oluşturuyoruz
pencere = turtle.Screen()
#2. sonra canvas elde ediyoruz
canvas = pencere.getcanvas()
#3. sonra en üst seviyeye ulaşıyoruz
root = canvas.winfo_toplevel()
pencere.bgcolor('#424242')
pencere.title('Uygulamayı Hatasız Kapatma')
pencere.setup(width=600, height=600)
pencere.tracer(0)
# sekil
sekil = turtle.Turtle()
sekil.shape('square')
sekil.shapesize(5, 2)
sekil.pu()
sekil.speed(0)
sekil.color('#efebe9', '#ff3d00')
sekil.goto(0, 0)
def kapat():
    global devam
    devam = False
#5. pencere kapatma olayını yakalıyoruz ve devam değişkenin değerini değiştirecek fonksiyonu çağırıyoruz
root.protocol('WM_DELETE_WINDOW', kapat)
# 4. boolean devam değişkeni tanımlıyoruz
devam = True
while devam:
    pencere.update()
    #x = random.randint(1, 200)
    #y = random.randint(1, 200)
    #sekil.goto(x, y)
'''terminalde
>pip  install pyinstaller
yazdıktan sonra;
>pyinstaller -F -w main.py
yazarak uygulama exe ye dönüştürelebilir.
'''