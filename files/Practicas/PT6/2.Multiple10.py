n=int(input("Escribe un numero"))
n2=n
i=0
while n%10!=0:
    n=int(input("Error, Introduce un numero"))
    n2=n
while n2%10==0:
    n2=n2//10
    i+=1
cabeza="{:<10}{:}\n".format("Entrada", "Sortida")
resultado=("{:<10}{} {} {}\n".format(n,n2,"per 10 elevat",i))
print(cabeza+resultado)
