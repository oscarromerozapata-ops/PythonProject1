agenda="Pedro*Balmes 27*111111111#333425325#+4534553453#;Jacinta*Ardur 32*333333333#657483746#;Andres*Arriba 1**444444444#374658365#;Anabel*Derecha 3**222222222#465768347#;"
contacto=""
datos=""
menu00="1)View contacts\n2)New contact\n3)Edit contact\n4)Remove contact\n5)Search contact\n6)salir"
menu03="1)Edit direction\n2)Add tfn\n3)Remove tfn\n4)back"
menu05="1)Search by name\n2)Search from direction\n3)Search by num\n4)back"
exi=False
flg_menu00=True
flg_menu03=False
flg_menu031=False
flg_menu04=False

flg_menu05=False
opciones=""
print(datos)
while not exi:
    while flg_menu00:
        print(menu00)
        opc=input("Escoge una opción")
        if not opc.isdigit():
            print("Opción incorrecta")
            input("Enter to continue")
        elif int(opc)<1 or int(opc)>6:
            print("Opción fuera de rango")
            input("Enter to continue")
        else:
            opc=int(opc)
            if opc==1:
                for i in range(0,agenda.count(";")):
                    if i==0:
                        inicio=0
                        final=agenda.find(";")
                    else:
                        inicio=final+1
                        final=agenda.find(";",inicio)
                    contacto=agenda[inicio:final]
                    primer_separador=contacto.find("*")
                    segundo_separador=contacto.find("*",primer_separador+1)
                    nombre=contacto[:primer_separador]
                    direccion=contacto[primer_separador+1:segundo_separador]
                    tfns=contacto[segundo_separador+1:]
                    print(agenda[inicio:final])
                    for j in range(tfns.count("#")):
                        if j==0:
                            inicio2=0
                            final2=tfns.find("#")
                            datos=datos+"{:<20}{:<20}{:>20}\n".format(nombre,direccion,tfns[inicio2:final2])
                        else:
                            inicio2=final2+1
                            final2=tfns.find("#",inicio2)
                            datos=datos+"{:>60}\n".format(tfns[inicio2:final2])
                    datos=datos+"-"*60+"\n"
                print(datos)

            elif opc==2:
                nombre=input("nombre")
                direccion=input("direccion")
                numero=input("numero")
                contacto=nombre+"*"+direccion+"*"+numero+"#;"
                salir=False
                while not salir:
                    opc = input("desea agregar a {} con la direccion {} y con el numero {} a tu lista de contactos? S/N".format(
                            nombre, direccion, numero))
                    if opc=="S":
                        agenda=agenda+contacto
                        salir = True
                    elif opc=="N":
                        input("Saliendo")
                        salir=True
                    else:
                        print("Opcion incorrecta")
            elif opc==3:
                flg_menu00=False
                flg_menu03=True
            elif opc==6:
                salir=True
                flg_menu00 = False
    while flg_menu03:
        print(menu03)
        opc = input("Escoge una opción")
        if not opc.isdigit():
            print("Opción incorrecta")
            input("Enter to continue")
        elif int(opc) < 1 or int(opc) > 4:
            print("Opción fuera de rango")
            input("Enter to continue")
        else:
            opc=int(opc)
            if opc==1:
                print("")

            elif opc==2:
                print("")

            elif opc==3:
                print("")
            elif opc==4:
                flg_menu00=True
                flg_menu03=False
    while flg_menu04:
        print("")

    while flg_menu05:
        print(menu05)
        opc=input("opció")
        if not opc.isdigit():
            print("Error introduce una opción numerica")
        elif int(opc)<1 or int(opc)>6:
            print("opción fuera de rango")
            input("Enter to continue")
        else:
            opc=int(opc)
            if opc==1:
                print("")

            elif opc == 2:
                print("")

            elif opc == 3:
                print("")

            elif opc==4:
                flg_menu00 = True
                flg_menu05 = False






