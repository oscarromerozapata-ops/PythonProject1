
cabecera="dni".ljust(10)+"nombre".ljust(20)+"Nota".rjust(5)+"\n"+"alumnes".center(35,"*")+"\n"

print(cabecera)

dni=input("Dni")
nombre=input("nombre")
nota=float(input("Nota"))
cuerpo=dni.ljust(10)+nombre.ljust(20)+nota.rjust(5.4f)+"\n"

print(cabecera+cuerpo)

cabecera="{:10}{:20}{:>5}".format("dni","nombre","Nota")+"\n"+"*"*35+"\n"

dni=input("Dni")
nombre=input("nombre")
nota=float(input("Nota"))
cuerpo+="{:10}{:20}{:>5.4f}".format(dni,nombre,nota)
print(cabecera+cuerpo)