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
flg_menu031=False
flg_menu04=False
flg_edit_contact=False
flg_borrar_telefono = False
flg_menu05=False
opciones=""
flg_menu04
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
                flg_menu00=False
                flg_menu04=True
            elif opc==5:
                flg_menu00=False
                flg_menu05=True
            elif opc == 6:
                flg_menu00 = False
                exi=True
    while flg_menu03:
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
                    datos = datos + str(j + 1) + ")" + "{:20}{:20}{:>20}\n".format(nombre, direccion,
                                                                                   tfns[inicio:final])
                else:
                    inicio = final + 1
                    final = tfns.find("#", inicio)
                    datos = datos + "{:20}{:20}{:>20}\n".format("", "", tfns[inicio:final])
            datos = datos + "-" * 60 + "\n"
        datos = datos + str(j + 2) + ")Salir\n"
        print(datos)
        datos = ""
        opc = input("Cual contacto desea editar")
        if not opc.isdigit():
            print("Error introduce una opción numerica")
        elif not int(opc) in range(1,agenda.count(";")+2):
            print("opción fuera de rango")
            input("Enter to continue")
        elif int(opc) == agenda.count(";")+1:
            flg_menu03 = False
            flg_menu00=True
        else:
            opc = int(opc)
            flg_edit_contact=True
            while flg_edit_contact:
                print(menu03)
                opc_edit = input("opció")
                if not opc_edit.isdigit():
                    print("Error introduce una opción numerica")
                elif not int(opc_edit) in range(1,5) :
                    print("opción fuera de rango")
                    input("Enter to continue")
                else:
                    opc_edit = int(opc_edit)
                    for i in range(0, agenda.count(";")):
                        if i == 0:
                            inicio = 0
                            final = agenda.find(";")
                        else:
                            inicio = final + 1
                            final = agenda.find(";", inicio)
                        if i == opc - 1:
                            contacto = agenda[inicio:final]
                            print(contacto)
                            primer_separador = contacto.find("*")
                            segundo_separador = contacto.find("*", primer_separador+1)
                            nombre = contacto[:primer_separador]
                            direccion = contacto[primer_separador + 1:segundo_separador]
                            tfns = contacto[segundo_separador+1:]

                            if opc_edit==1:
                                #editar direccion
                                nueva_direccion = input("Nueva direccion")
                                agenda=agenda[:inicio]+nombre+"*"+nueva_direccion+"*"+tfns+";"+agenda[final+1:]
                                print(agenda)
                            elif opc_edit==2:
                                #add tfn
                                nuevo_telefono = input("Nueva telefono")
                                agenda=agenda[:inicio]+nombre+"*"+direccion+"*"+tfns+nuevo_telefono+"#;"+agenda[final+1:]
                                print(agenda)
                            elif opc_edit==3:
                                #remove tfn
                                flg_borrar_telefono = True
                                while flg_borrar_telefono:
                                    menu_telefono ="Borrar telefono".center(30,"*")+"\n"
                                    for j in range(tfns.count("#")):
                                        if j == 0:
                                            inicio3=0
                                            final3=tfns.find("#")
                                        else:
                                            inicio3=final3+1
                                            final3=tfns.find("#", inicio3)
                                        menu_telefono+=str(j+1)+")"+tfns[inicio3:final3]+"\n"
                                    menu_telefono=menu_telefono+str(j+2)+")Salir"
                                    print(menu_telefono)
                                    opc=input("Cual telefono desea eliminar")
                                    if not opc.isdigit():
                                        print("Error introduce una opcion numerica")
                                        input("Enter to continue")
                                    elif not int(opc) in range(1,tfns.count("#")+2):
                                        print("opcion fuera de rango")
                                        input("Enter to continue")
                                    else:
                                        opc=int(opc)
                                        if opc == tfns.count("#")+1:
                                            flg_borrar_telefono=False
                                        else:
                                            for k in range(0, tfns.count("#")):
                                                if k == 0:
                                                    inicio2 = 0
                                                    final2 = tfns.find("#")
                                                else:
                                                    inicio2 = final2 + 1
                                                    final2 = tfns.find("#", inicio2)
                                                if k+1 == opc:
                                                    tfns = tfns[:inicio2]+tfns[final2+1:]
                                                    agenda=agenda[:inicio]+nombre+"*"+direccion+"*"+tfns+";"+agenda[final+1:]
                                                    break
                                            print(agenda)

                            elif opc_edit==4:
                                flg_edit_contact=False
                            break
    while flg_menu04:
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
                    datos = datos + str(j + 1) + ")" + "{:20}{:20}{:>20}\n".format(nombre, direccion,
                                                                                   tfns[inicio:final])
                else:
                    inicio = final + 1
                    final = tfns.find("#", inicio)
                    datos = datos + "{:20}{:20}{:>20}\n".format("", "", tfns[inicio:final])
            datos = datos + "-" * 60 + "\n"
        datos = datos + str(j + 2) + ")Salir\n"
        salir = str(j + 2)
        print(datos)
        datos = ""
        opc = input("Cual contacto desea eliminar")
        if not opc.isdigit():
            print("Error introduce una opción numerica")
        elif not int(opc) in range(1, agenda.count(";") + 2):
            print("opción fuera de rango")
            input("Enter to continue")
        else:
            opc = int(opc)
            if opc == agenda.count(";") + 1:
                flg_menu04 = False
                flg_menu00 = True
            else:
                inicio = 0
                final = 0
                for j in range(opc):
                    if j == 0:
                        inicio = 0
                        final = agenda.find(";")
                    else:
                        inicio = final + 1
                        final = agenda.find(";", inicio)
                    contacto = agenda[inicio:final]
                print(contacto)
                agenda = agenda[:inicio] + agenda[final + 1:]
                print(agenda)
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
                buscar = input("Buscar contacto")
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
                    if buscar.lower() in nombre.lower():
                        for i in range(0, tfns.count("#")):
                            if i == 0:
                                inicio = 0
                                final = tfns.find("#")
                                datos = datos + "{:20}{:20}{:>20}\n".format(nombre, direccion,
                                                                            tfns[inicio:final])
                            else:
                                inicio = final + 1
                                final = tfns.find("#", inicio)
                                datos = datos + "{:20}{:20}{:>20}\n".format("", "", tfns[inicio:final])
                        datos = datos + "-" * 60 + "\n"
                print(datos)
            elif opc == 2:
                direc = input("Buscar direccion")
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
                    if direc.lower() in direccion.lower():
                        for i in range(0, tfns.count("#")):
                            if i == 0:
                                inicio = 0
                                final = tfns.find("#")
                                datos = datos + "{:20}{:20}{:>20}\n".format(nombre, direccion,
                                                                            tfns[inicio:final])
                            else:
                                inicio = final + 1
                                final = tfns.find("#", inicio)
                                datos = datos + "{:20}{:20}{:>20}\n".format("", "", tfns[inicio:final])
                        datos = datos + "-" * 60 + "\n"
                print(datos)
            elif opc == 3:
                num = input("Buscar por numero")
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
                    if num.lower() in tfns.lower():
                        for i in range(0, tfns.count("#")):
                            if i == 0:
                                inicio = 0
                                final = tfns.find("#")
                                datos = datos + "{:20}{:20}{:>20}\n".format(nombre, direccion,
                                                                            tfns[inicio:final])
                            else:
                                inicio = final + 1
                                final = tfns.find("#", inicio)
                                datos = datos + "{:20}{:20}{:>20}\n".format("", "", tfns[inicio:final])
                        datos = datos + "-" * 60 + "\n"
                print(datos)
            elif opc==4:
                flg_menu00 = True
                flg_menu05 = False
