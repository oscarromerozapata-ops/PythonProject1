a1=1
a2=2
a3=3
d1=6
d2=5
atacante=0
defensor=0
aux=0
if a1<a2:
    aux=a1
    a1=a2
    a2=aux
if a1<a3:
    aux=a1
    a1=a3
    a3 = aux
if a2<a3:
    aux=a2
    a2=a3
    a3=aux
if d1<d2:
    aux=d1
    d1=d2
    d2=aux

if a1>d1:
    atacante+=1
elif a1<=d1:
    defensor+=1
if a2>d2:
    atacante+=1
elif a2<=d2:
    defensor+=1

tabla="{:20}{:10}{:10}{:10}{:10}".format("Jugador","Dado1","Dado2","Dado3", "Puntos")+"\n"+\
      "*"*60+"\n"+\
      "{:20}{:<10}{:<10}{:<10}{:<10}".format("Atacante",a1,a2,a3,atacante)+"\n"+\
      "{:20}{:<10}{:<10}{:<10}{:<10}".format("Defensor",d1,d2,"",defensor)


print(tabla)