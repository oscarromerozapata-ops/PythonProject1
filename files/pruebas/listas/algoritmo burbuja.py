import random
lista=[]
aux=0

for i in range(5):
    lista.append(random.randint(0,100))
print (lista)

for pasada in range(len(lista)-1):
    ordenado=True
    for i in range(len(lista)-1-pasada):
        if lista[i]>lista[i+1]:
            ordenado=False
            aux=lista[i]
            lista[i]=lista[i+1]
            lista[i+1]=aux
        print(lista)
    if ordenado:
        break

        print(lista[i],"   ", lista[i+1])
print(lista)