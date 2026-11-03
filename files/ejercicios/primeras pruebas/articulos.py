cabecera= (("Lista de la compra").center(40,"*")+
           "\n"+str("Articulos").ljust(20)+str("cantidad").rjust(10)+str("precio").rjust(10)+"\n"+ "*" *40)+"\n"
a1=input("primer aticulo")
c1=int(input("cantidad"))
p1 = float(input("precio"))
cadena= "{:<20}{:>10}{:10.2f}".format(a1,c1,p1)+"\n"

print(cabecera+cadena)
a1=input("primer aticulo")
c1=int(input("cantidad"))
p1 = float(input("precio"))
cadena+= "{:<20}{:>10}{:10.2f}".format(a1,c1,p1)+"\n"

print(cabecera+cadena)
a1=input("primer aticulo")
c1=int(input("cantidad"))
p1 = float(input("precio"))
cadena+= "{:<20}{:>10}{:10.2f}".format(a1,c1,p1)+"\n"
print(cabecera+cadena)