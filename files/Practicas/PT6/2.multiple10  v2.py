n=input("Escribe un numero multiple de 10")
while not n.isdigit() or int(n)%10!=0:
    if not n.isdigit():
        n = input("Error, Introduce un numero multiple de 10")
    elif int(n)%10!=0:
        n = input("Error, Introduce un numero multiple de 10")
n=int(n)
n2=n
i=0
while n2%10==0:
    n2=n2//10
    i+=1
cabeza="{:<10}{:}\n".format("Entrada", "Sortida")
resultado=("{:<10}{} {} {}\n".format(n,n2,"per 10 elevat",i))
print(cabeza+resultado)
