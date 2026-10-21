import random

num=random.randrange(1,101)
resp=0
cont=0
print(num)
while not cont==5:
    cont+=1
    resp=int(input("Dame un número"))
    if resp>num:
        print("El número es mas pequeño")
    elif resp<num:
        print("número mas grande")
    else:
        print("has acertado")
