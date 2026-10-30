salir=False
numeros=0
contador=0
while not salir:
    num=int(input("Digite un numero: "))
    if num==-1:
        break
    else:
        numeros=numeros+num
        contador=contador+1
mitjana=numeros/contador
print("mitjana aritmetica: ", mitjana)
