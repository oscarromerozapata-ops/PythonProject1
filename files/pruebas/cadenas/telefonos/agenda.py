agenda="Pedro*Balmes 27*111111111#333425325#+4534553453#;Jacinta*Ardur 32*333333333#657483746#;Andres*Arriba 1**444444444#374658365#;Anabel*Derecha 3**222222222#465768347#;"
contacto= "Pedro*Balmes 27*111111111#333425325#+4534553453#"
datos=""
menu00="1)Añadir contacto\n2)Ver contacto\n3)salir"
salir=False
flg_menu00=True
for j in range (0,agenda.count(";")):
    if j ==0:
        inicio2=0
        final2=agenda.find(";")
    else:
        inicio2=final2+1
        final2=agenda.find(";",inicio2)
    contacto=agenda[inicio2:final2]
    primer_separador=contacto.find("*")
    segundo_separador=contacto.find("*",primer_separador+1)
    nombre=contacto[:primer_separador]
    direccion=contacto[primer_separador+1:segundo_separador]
    tfns=contacto[segundo_separador+1:]

    for i in range (0,tfns.count("#")):
        if i ==0:
            inicio=0
            final=tfns.find("#")
            datos = datos + "{:20}{:20}{:>20}\n".format(nombre, direccion, tfns[inicio:final])
        else:
            inicio=final+1
            final=tfns.find("#",inicio)
            datos = datos + "{:20}{:20}{:>20}\n".format("", "", tfns[inicio:final])
while not salir:
    while flg_menu00:
        print(menu00)
        opc=input("opció")
        if not opc.isdigit():
            print("Error introduce una opción numerica")
        elif int(opc)>0 or int(opc)>4:
            print("opción fuera de rango")
        else:

            if opc==1:
            contacto=input("introduce nomrbe del contacto")
            contacto=contacto+"*"
            contacto
            for x in range(0, tfns.count("#")):
                if x == 0:
                    inicio = 0
                    final = tfns.find("#")
                    datos = datos + "{:20}{:20}{:>20}\n".format(nombre, direccion, tfns[inicio:final])
                else:
                    inicio = final + 1
                    final = tfns.find("#", inicio)
                    datos = datos + "{:20}{:20}{:>20}\n".format("", "", tfns[inicio:final])







print(datos)