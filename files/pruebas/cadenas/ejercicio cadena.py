cadena="gonzalo.asd.g@gmail.com"

valido=True
print(cadena.find("@"))
if cadena.find("@")==-1:
    print("falta @")
    valido=False
else:
    pos=cadena.find("@")
    nombre=cadena[:pos]
    dominio=cadena[pos+1:]

    if nombre=="" or nombre=="@" or nombre[0]=="." or nombre[-1]=="." or nombre.find("..")!=-1:
        valido=False
    if dominio=="" or dominio=="@" or dominio[0]=="." or dominio[-1]=="." or dominio.find("..")!=-1:
        valido=False






print(valido)