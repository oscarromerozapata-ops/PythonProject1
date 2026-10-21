import random
d1=0
d2=0
d3=0
d4=0
d5=0
dd1=0
dd2=0
dd3=0
puntos_a=0
puntos_d=0

for i in range(6):
    da=random.randrange(1,6)
    if da>d1:
        aux=d1
        d1=da
        da=aux
    if da>d2:
        aux=d2
        d2=da
        da=aux
    if da>d3:
        aux=d3
        d3=da
        da=aux
    if da>d4:
        aux=d4
        d4=da
        da=aux
    if da>d5:
        aux=d5
        d5=da
        da=aux
for j in range(3):
    dd = random.randrange(1, 7)
    if dd>dd1:
        aux=dd1
        dd1=dd
        dd=aux
    if dd>dd2:
        aux=dd2
        dd2=dd
        dd=aux
    if dd>dd3:
        aux=dd3
        dd3=dd
        dd=aux
if dd1>=d1:
    print("Defensor +1p")
    puntos_d+=1
else:
    print("Atacante +1p")
    puntos_a += 1
if dd2>=d2:
    print("Defensor +1p")
    puntos_d += 1
else:
    print("Atacante +1p")
    puntos_a += 1
if dd3>=d3:
    print("Defensor +1p")
    puntos_d += 1
else:
    print("Atacante +1p")
    puntos_a += 1
if puntos_a>puntos_d:
    ganar="Gana el atacante"
else:
    ganar="Gana el defensor"
print (d1,d2,d3,d4,d5,"\n",dd1,dd2,dd3,puntos_d,puntos_a)
menu= ("DADOS".center(35,"=")+"\n"+
    "{:15}{:3}{:3}{:3}{:3}{:3}\n".format("Dados Atacante:",d1,d2,d3,d4,d5)+
    "{:15}{:3}{:3}{:3}{:3}{:3}\n".format("Dados Defensor:",dd1,dd2,dd3,"","")+
    "PUNTOS".center(35,"=")+"\n"+
    "Puntos Atacante: {}\n".format(puntos_a)+
    "Puntos Defensor: {}\n".format(puntos_d)+
    "="*35+"\n"+
    ganar
    )
print (menu)