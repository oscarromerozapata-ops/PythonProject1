agenda="Pedro*Balmes 27*111111111#333425325#+4534553453#;Jacinta*Ardur 32*333333333#657483746#;Andres*Arriba 1**444444444#374658365#;Anabel*Derecha 3**222222222#465768347#;"
contacto=""
datos=""
menu00="1)View contacts\n2)New contact\n3)Edit contact\n4)Remove contact\n5)Search contact\n6)salir"
menu03="1)Edit direction\n2)Add tfn\n3)Remove tfn\n4)back"
menu05="1)Search by name\n2)Search from direction\n3)Search by num\n4)back"
exi=False
salir=False
flg_menu00=True
flg_menu03=False
flg_menu05=False
opciones=""

print(datos)
while not exi:
    while flg_menu00:
        print(menu00)
        opc=input("opció")
        if not opc.isdigit():
            print("Error introduce una opción numerica")
        elif int(opc)<1 or int(opc)>6:
            print("opción fuera de rango")
            input("Enter to continue")
        else:
            opc=int(opc)
            if opc==1:
                for j in range(0, agenda.count(";")):
                    if j == 0:
                        inicio2 = 0
                        final2 = agenda.find(";")
                    else:
                        inicio2 = final2 + 1
                        final2 = agenda.find(";", inicio2)
                    contacto = agenda[inicio2:final2]
                    primer_separador = contacto.find("*")
                    segundo_separador = contacto.find("*", primer_separador + 1)
                    nombre = contacto[:primer_separador]
                    direccion = contacto[primer_separador + 1:segundo_separador]

                    tfns = contacto[segundo_separador + 1:]

                    for i in range(0, tfns.count("#")):
                        if i == 0:
                            inicio = 0
                            final = tfns.find("#")
                            datos = datos + str(j+1)+")"+"{:20}{:20}{:>20}\n".format(nombre, direccion, tfns[inicio:final])
                        else:
                            inicio = final + 1
                            final = tfns.find("#", inicio)
                            datos = datos +"{:20}{:20}{:>20}\n".format("", "", tfns[inicio:final])
                    datos = datos + "-"*60+"\n"
                print(datos)
                datos=""
                input("Enter to continue")
            elif opc==2:
                nombre = input("introduce nombre del contacto")
                direccion = input("introduce una dirección")
                tel = True
                numero=""
                while tel:
                    numero = numero+input("introduce un numero de telefono")
                    numero=numero + "#"
                    opcion=input("Deseas agregar otro numero de telefono S/N")
                    if opcion=="N":
                        tel=False
                    elif opcion=="S":
                        tel=True
                    else:
                        print("introduce S/N")
                opc=input("Deseas agregar a {} de {} con el numero {} a tu lista de contactos? S/N".format(nombre, direccion,numero))
                if opc=="S":
                    contacto = nombre + "*"+direccion+"*"+numero+";"
                    agenda=agenda+contacto
                contacto=""
                print (agenda)
            elif opc==3:
                flg_menu00=False
                flg_menu03=True
            elif opc==4:
                for j in range(0, agenda.count(";")):
                    if j == 0:
                        inicio2 = 0
                        final2 = agenda.find(";")
                    else:
                        inicio2 = final2 + 1
                        final2 = agenda.find(";", inicio2)
                    contacto = agenda[inicio2:final2]
                    primer_separador = contacto.find("*")
                    segundo_separador = contacto.find("*", primer_separador + 1)
                    nombre = contacto[:primer_separador]
                    direccion = contacto[primer_separador + 1:segundo_separador]

                    tfns = contacto[segundo_separador + 1:]

                    for i in range(0, tfns.count("#")):
                        if i == 0:
                            inicio = 0
                            final = tfns.find("#")
                            datos = datos + str(j+1)+")"+"{:20}{:20}{:>20}\n".format(nombre, direccion, tfns[inicio:final])
                        else:
                            inicio = final + 1
                            final = tfns.find("#", inicio)
                            datos = datos +"{:20}{:20}{:>20}\n".format("", "", tfns[inicio:final])
                    datos = datos + "-"*60+"\n"
                datos = datos + str(j + 2) + ")Salir\n"
                salir = str(j + 2)
                print(datos)
                opc=int(input("Cual contacto desea eliminar"))
                if not opc==int(salir):
                    inicio3 = agenda.find(";",opc)
                    final3 = agenda.find(";", inicio3)
                    agenda = agenda[:inicio3] + agenda[final3 + 1:]
                print(agenda)
                datos=""
            elif opc==5:
                flg_menu00=False
                flg_menu05=True
            elif opc == 6:
                flg_menu00 = False
                exi=True
    while flg_menu03:
        print(menu03)
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
            elif opc==2:
                print("")
            elif opc==3:
                print("")
            elif opc==4:
                flg_menu00 = True
                flg_menu03 = False
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
            elif opc==4:
                flg_menu00 = True
                flg_menu05 = False



# for j in range (0,agenda.count(";")):
#     if j == 0:
#         inicio2=0
#         final2=agenda.find(";")
#     else:
#         inicio2=final2+1
#         final2=agenda.find(";",inicio2)
#     contacto=agenda[inicio2:final2]
#     primer_separador=contacto.find("*")
#     segundo_separador=contacto.find("*",primer_separador+1)
#
#     nombre=contacto[:primer_separador]
#     direccion=contacto[primer_separador+1:segundo_separador]
#     tfns=contacto[segundo_separador+1:]
#     opciones = opciones + str(j + 1) + ")" + "{:20}{:20}\n".format(nombre, direccion)
# opciones = opciones + str(j + 2) + ")" + "{:20}{:20}\n".format(nombre, direccion)
#     for i in range (0,tfns.count("#")):
#         if i ==0:
#             inicio=0
#             final=tfns.find("#")
#             datos = datos + "{:20}{:20}{:>20}\n".format(nombre, direccion, tfns[inicio:final])
#         else:
#             inicio=final+1
#             final=tfns.find("#",inicio)
#             datos = datos + "{:20}{:20}{:>20}\n".format("", "", tfns[inicio:final])
#     datos=datos+"-"*60+"\n"