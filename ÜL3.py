# 3.ülesanne
# Kärt 05.12.24
import turtle

#3.1
nimi = "Imre" #sõne, string, str
vanus = 20 #int, interger, täisarv
keskmine_hinne = 6.5 #komaarv, float
#plussiga saan stringid kokku
print(nimi+", "+str(vanus)+" aastat vana ja keskmine hinne on "+str(keskmine_hinne))
#komaga saan mitu asja printida
print(nimi, vanus, keskmine_hinne)
#lause vormindamine lünkadega
print(f"Jüri on {vanus} aastat vana ja keskmine hinne on {keskmine_hinne}")

#3.7 kolmnurk
kylje_pikkus = 20
nurk = 120
varv = "red"

turtle.speed(0) # reguleeri 1-9
turtle.color(varv)
#kolmnurk1
turtle.forward(kylje_pikkus) #fd, pikslites
turtle.left(nurk) #lt, rt
turtle.forward(kylje_pikkus) #fd, pikslites
turtle.left(nurk) #lt, rt
turtle.forward(kylje_pikkus) #fd, pikslites
turtle.left(nurk) #lt, rt

turtle.penup()
turtle.goto(kylje_pikkus*1.5,0)
turtle.pendown()

#kolmnurk2
turtle.forward(kylje_pikkus) #fd, pikslites
turtle.left(nurk) #lt, rt
turtle.forward(kylje_pikkus) #fd, pikslites
turtle.left(nurk) #lt, rt
turtle.forward(kylje_pikkus) #fd, pikslites
turtle.left(nurk) #lt, rt

turtle.penup()
turtle.goto(kylje_pikkus*3,0)
turtle.pendown()

#kolmnurk3
turtle.forward(kylje_pikkus) #fd, pikslites
turtle.left(nurk) #lt, rt
turtle.forward(kylje_pikkus) #fd, pikslites
turtle.left(nurk) #lt, rt
turtle.forward(kylje_pikkus) #fd, pikslites
turtle.left(nurk) #lt, rt


