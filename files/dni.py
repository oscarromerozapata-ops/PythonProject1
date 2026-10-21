cabecera= (("Datos Clientes").center(40,"*")+
           "\n"+str("Nombre").ljust(20)+str("Edad")+"  "+str("Dni").rjust(5)+str("TLF").rjust(15)+"\n"+ "*" *40)+"\n"

print(cabecera)
n=input("nombre")
e=input("Edad")
d=input("Dni")
t=input("Telefono")
cadena=(n.ljust(20)+e.rjust(5)+"  "+d.ljust(15)+t.ljust(10))+"\n"
print(cabecera+cadena)

cabecera= "Datos Clientes".center(40,"*")+"\n"+\
           "{:<20}{:<5}  {:15}{:<10}".format("Nombre","Edad","Dni","TLF")+"\n"
n=input("nombre")
e=input("Edad")
d=input("Dni")
t=input("Telefono")
cadena+= "{:<20}{:<5}  {:15}{:<10}".format(n,e,d,t)+"\n"

print(cabecera+cadena)

