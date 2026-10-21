
cadena= "Maria;Pedro Sebastian;Anabel;Andres;"
#print(cadena.count(";"))


longitud_inicial=len(cadena)
nueva_cadena=""
for i in range(0,cadena.count(";")):
    if i ==0:
        inicio=0
        final=cadena.find(";")
    else:
        inicio=final+1
        final=cadena.find(";",inicio)
    nombre=cadena[inicio:final]
    #insertamos nombre nueva cadena
    if len(nueva_cadena)==0:
        nueva_cadena=nombre+";"
    else:
        longitud_inicial=len(nueva_cadena)
        for j in range(0, nueva_cadena.count(";")):
            if j == 0:
                inicio2 = 0
                final2 = nueva_cadena.find(";")
            else:
                inicio2 = final2 + 1
                final2 = nueva_cadena.find(";", inicio2)
            nombre2 = nueva_cadena[inicio2:final2]
            if nombre<nombre2:
                nueva_cadena= nueva_cadena[:inicio2]+nombre+";"+nueva_cadena[inicio2:]
                break
        if len(nueva_cadena)==longitud_inicial:
            nueva_cadena=nueva_cadena+nombre+";"
cadena=nueva_cadena
print(cadena)




