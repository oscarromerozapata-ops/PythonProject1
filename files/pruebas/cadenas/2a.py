nombre_incluir="Esteban"
cadena= "Anabel;zndres;Lucia;Paco;Pedro;"
nombre=""
#print(cadena.count(";"))


longitud_inicial=len(cadena)
for i in range(0,cadena.count(";")):
    if i ==0:
        inicio=0
        final=cadena.find(";")
    else:
        inicio=final+1
        final=cadena.find(";",inicio)
    nombre=cadena[inicio:final]

    print(nombre_incluir<nombre)
    if nombre_incluir<nombre:
        cadena=cadena[:inicio]+nombre_incluir+";"+cadena[inicio:]
        break
if len(cadena)==longitud_inicial:
    cadena=cadena+nombre_incluir+";"
print(cadena)



