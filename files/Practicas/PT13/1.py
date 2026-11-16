lista=[2.3, 5.6, 7.2, 5.0, 3.0 ,2.1 ]

print(lista)
for i in range (len(lista)-1,-1,-1):
    print(lista[i])

lista[2]=6
print(lista)

for i in range (len(lista)):
    if i%2==0:
        print(lista[i])
print("*"*30)
for i in range (len(lista)):
    if i%2==1:
        print(lista[i])