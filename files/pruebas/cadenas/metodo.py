cadena= "Pedro;Paco;Anabel;Lucia;Andres;"

print(cadena.count(";"))

for i in range(0,cadena.count(";")):
    nombre=""
    if i ==0:
        inicio=0
        final=cadena.find(";")
    else:
        inicio=final+1
        final=cadena.find(";",inicio)
    nombre=cadena[inicio:final]
    print (nombre)