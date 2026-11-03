nombre_incluir="Esteban"
cadena= "Anabel;zndres;Lucia;Paco;Pedro;"
nombre=""
#print(cadena.count(";"))



for i in range(0,cadena.count(";")+1):
    if i ==0:
        inicio=0
        final=cadena.find(";")
    else:
        inicio=final+1
        final=cadena.find(";",inicio)
    nombre=cadena[inicio:final]
    if nombre>nombre_incluir and not nombre_incluir=="":
        print(nombre_incluir)
        nombre_incluir=""
    print(nombre)



