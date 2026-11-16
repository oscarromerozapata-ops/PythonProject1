import random
lista=[]
aux=0

for i in range(5):
    lista.append(random.randint(0,100))
print (lista)

for i in range(len(lista)-1):
    for j in range(i+1,len(lista)):
        if lista[i]<lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux

print(lista)
