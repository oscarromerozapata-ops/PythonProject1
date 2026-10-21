cadena = "Pedro*111111111;Anabel*222222222;Jacinta*333333333;Andres*444444444;"

for i in range(0,cadena.count(";")):
    nombre=""
    if i ==0:
        inicio=0
        final=cadena.find(";")
    else:
        inicio=final+1
        final=cadena.find(";",inicio)
    nombre=cadena[inicio:final]
    print(nombre)
    asterisco=nombre.find("*")
    print (nombre.replace("*","     "))
    # for j in range(0, cadena.count(";")):
    #     num = ""
    #     if j == 0:
    #         inicio2 = cadena.find("*")
    #         final2 = cadena.find(";")
    #     else:
    #         inicio2 = final2 + 1
    #         final2 = cadena.find(";", inicio2)
    #     num = cadena[inicio2:final2]
    #     print(num)
    #     break
