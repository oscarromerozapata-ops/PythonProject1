num=input("Cuantos numeros vas a introducir?")
while not num.isdigit():
    num = input("Error, Cuantos numeros vas a introducir?")
num=int(num)
i=0
datos=0
mayor=0
menor=999999999999
suma=0
c=num
while num!=0:
    num=num-1
    datos=int(input("introdueix un numero"))
    suma+=datos
    if datos>mayor:
        aux=datos
        mayor=datos
        datos=aux
    if datos<menor:
        menor=datos
        continue
mitjana=suma/c
print("El numero mayor es: ",mayor,"\nEl numero menor es: ",menor,"\nLa mitjana es:",mitjana)




