salir=False
maxim=0
minim=99999999999999999999
contador=0
numeros=0
while not salir:
    num=int(input("ingrese un numero: "))
    if num==0:
        break
    contador=contador+1
    numeros=numeros+num
    mitjana=numeros/contador
    if num>maxim:
        maxim=num
    if num<minim:
        minim=num
print("Maxim = ",maxim, "Minim = ", minim, "Mitjana = ", mitjana)