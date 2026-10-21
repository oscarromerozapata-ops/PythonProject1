num=int(input("Dona'm un número"))

div=1
datos=""
for i in range(num):
    div+=1
    if num%div==0:
        datos=datos+str(div)+" "
print("Els divisors son: ",datos)