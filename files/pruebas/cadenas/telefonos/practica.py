agenda="Pedro*Balmes 27*111111111#333425325#+4534553453#;Jacinta*Ardur 32*333333333#657483746#;Andres*Arriba 1**444444444#374658365#;Anabel*Derecha 3**222222222#465768347#;"
contacto=""
datos=""
menu00="1)View contacts\n2)New contact\n3)Edit contact\n4)Remove contact\n5)Search contact\n6)salir"
menu03="1)Edit direction\n2)Add tfn\n3)Remove tfn\n4)back"
menu05="1)Search by name\n2)Search from direction\n3)Search by num\n4)back"
salir=False
flg_00=True
flg_03=False
flg_05=False
flg_edit_contact=False
flg_menu05=False
opciones=""
print(datos)
while not salir:
    while flg_00:
        print(menu00)
        opc=input("Escoge una opción")
        if not opc.isdigit():
            print("Opción incorrecta")
            input("Enter to continue")
        elif opc in range(1,7):
            print("Opción fuera de rango")
            input("Enter to continue")
        else:
            opc=int(opc)
            if opc==1:
                #View contacts
                for i in range(agenda.count(";")):
                    if i ==0:
                        inicio=0
                        final=agenda.find(";")
                    else:
                        inicio=final+1
                        final=agenda.find(";",inicio)
                    contacto=agenda[inicio:final]
                    primer_separador=contacto.find("*")
                    segundo_separador=contacto.find("*", primer_separador+1)
                    nombre=contacto[:primer_separador]
                    direccion=contacto[primer_separador+1:segundo_separador]
                    telefono=contacto[segundo_separador+1:]
                    for j in range(telefono.count("#")):
                        if j ==0:
                            inicio2=0
                            final2=telefono.find("#")
                            datos = datos + "{:<20}{:<20}{:>20}\n".format(nombre, direccion, telefono[inicio2:final2])
                        else:
                            inicio2=final2+1
                            final2=telefono.find("#", inicio2)
                            datos = datos + "{:>60}\n".format(telefono[inicio2:final2])
                    datos=datos+"-"*60+"\n"
                print(datos)
                datos=""
            elif opc==2:
                #New contact
                nombre=input("nombre")
                direccion=input("direccion")
                numero=input("numero")
                agenda=agenda+nombre+"*"+direccion+"*"+numero+"#;"
            elif opc==3:
                #Edit contact
                flg_00=False
                flg_03=True
            elif opc==4:
                #Remove contact
                flg_remove_contact=True
                while flg_remove_contact:
                    for i in range(agenda.count(";")):
                        if i==0:
                            inicio=0
                            final=agenda.find(";")
                        else:
                            inicio=final+1
                            final=agenda.find(";", inicio)
                        contacto = agenda[inicio:final]
                        primer_separador = contacto.find("*")
                        segundo_separador = contacto.find("*", primer_separador + 1)
                        nombre = contacto[:primer_separador]
                        direccion = contacto[primer_separador + 1:segundo_separador]
                        telefono = contacto[segundo_separador + 1:]
                        for j in range(telefono.count("#")):
                            if j == 0:
                                inicio2 = 0
                                final2 = telefono.find("#")
                                datos = datos + "{:1}{:2}{:<20}{:<20}{:>20}\n".format(str(i + 1), ")", nombre, direccion,
                                                                                      telefono[inicio2:final2])
                            else:
                                inicio2 = final2 + 1
                                final2 = telefono.find("#", inicio2)
                                datos = datos + "{:>63}\n".format(telefono[inicio2:final2])
                        datos = datos + "-" * 60 + "\n"
                    datos = datos + str(i + 2) + ")Exit\n"
                    print(datos)
                    datos = ""
                    opc=input("Cual contacto desea eliminar")
                    if not opc.isdigit():
                        print("opcion no valida")
                        input("Enter to continue")
                    elif not int(opc) in range (1,agenda.count(";")+2):
                        print("opcion no valida")
                        input("enter to continue")
                    else:
                        opc=int(opc)
                        if opc==agenda.count(";")+1:
                            flg_remove_contact=False
                        else:
                            for i in range(agenda.count(";")):
                                if i==0:
                                    inicio=0
                                    final=agenda.find(";")
                                else:
                                    inicio=final+1
                                    final=agenda.find(";", inicio)
                                if i+1==opc:
                                    agenda=agenda[:inicio]+agenda[final+1:]
                                    print(agenda)
                                    break
            elif opc==5:
                #Search contact
                flg_05=True
                flg_00=False
            elif opc==6:
                salir=True
                flg_00 = False
    while flg_03:
        for i in range(agenda.count(";")):
            if i ==0:
                inicio=0
                final=agenda.find(";")
            else:
                inicio=final+1
                final=agenda.find(";",inicio)
            contacto=agenda[inicio:final]
            primer_separador=contacto.find("*")
            segundo_separador=contacto.find("*", primer_separador+1)
            nombre=contacto[:primer_separador]
            direccion=contacto[primer_separador+1:segundo_separador]
            telefono=contacto[segundo_separador+1:]
            print(contacto)
            for j in range(telefono.count("#")):
                if j == 0:
                    inicio2 = 0
                    final2 = telefono.find("#")
                    datos = datos + "{:1}{:2}{:<20}{:<20}{:>20}\n".format(str(i+1),")",nombre, direccion, telefono[inicio2:final2])
                else:
                    inicio2 = final2 + 1
                    final2 = telefono.find("#", inicio2)
                    datos = datos + "{:>63}\n".format(telefono[inicio2:final2])
            datos = datos + "-" * 60 + "\n"
        datos=datos+str(i+2)+")Exit\n"
        print(datos)
        datos = ""
        opc=input("Option")
        if not opc.isdigit():
            print("Opcion fuera de rango")
            input("Enter to continue")
        elif not int(opc) in range (1,agenda.count(";")+2):
            print("Opcion fuera de rango")
            input("Enter to continue")
        else:
            opc=int(opc)
            if opc==agenda.count(";")+1:
                flg_03 = False
                flg_00=True
            else:
                flg_edit_contact=True
            while flg_edit_contact:
                for k in range(agenda.count(";")):
                    if k==0:
                        inicio3=0
                        final3=agenda.find(";")
                    else:
                        inicio3=final3+1
                        final3=agenda.find(";",inicio3)
                    if k+1==opc:
                        contacto=agenda[inicio3:final3]
                        primer_separador=contacto.find("*")
                        segundo_separador=contacto.find("*", primer_separador+1)
                        nombre=contacto[:primer_separador]
                        direccion=contacto[primer_separador+1:segundo_separador]
                        tfns=contacto[segundo_separador+1:]
                        print(contacto)
                        break
                print(menu03)
                opc_edit = input("Escoge una opción")
                if not opc_edit.isdigit():
                    print("Opción incorrecta")
                    input("Enter to continue")
                elif int(opc_edit) < 1 or int(opc_edit) > 4:
                    print("Opción fuera de rango")
                    input("Enter to continue")
                else:
                    opc_edit = int(opc_edit)
                    if opc_edit == 1:
                        # Edit direction
                        nueva_direccion="patata"
                        agenda=agenda[:inicio3]+nombre+"*"+nueva_direccion+"*"+tfns+";"+agenda[final3+1:]
                        print(agenda)

                    elif opc_edit == 2:
                        # Add tfn
                        nuevo_tel="6969696969"
                        agenda=agenda[:inicio3]+nombre+"*"+direccion+"*"+tfns+nuevo_tel+"#;"+agenda[final3+1:]

                    elif opc_edit == 3:
                        # Remove
                        flg_borrar_tel=True
                        while flg_borrar_tel:
                            menu_borrar_tel="Delete tel".center(30,"*")+"\n"
                            for k in range(agenda.count(";")):
                                if k == 0:
                                    inicio = 0
                                    final = agenda.find(";")
                                else:
                                    inicio = final + 1
                                    final = agenda.find(";", inicio)
                                if k + 1 == opc:
                                    contacto = agenda[inicio:final]
                                    primer_separador = contacto.find("*")
                                    segundo_separador = contacto.find("*", primer_separador + 1)
                                    nombre = contacto[:primer_separador]
                                    direccion = contacto[primer_separador + 1:segundo_separador]
                                    tfns = contacto[segundo_separador + 1:]
                                    break
                            for i in range(tfns.count("#")):
                                if i==0:
                                    inicio2=0
                                    final2=tfns.find("#", inicio2)

                                else:
                                    inicio2=final2+1
                                    final2=tfns.find("#", inicio2)
                                menu_borrar_tel = menu_borrar_tel+str(i+1)+")"+tfns[inicio2:final2]+"\n"
                            menu_borrar_tel = menu_borrar_tel+str(i+2)+")Salir\n"
                            print(menu_borrar_tel)
                            opc_borrar=input("Option")
                            if not opc_borrar.isdigit():
                                print("Opcion fuera de rango")
                                input("Enter to continue")
                            elif not int(opc_borrar) in range(1,tfns.count("#")+2):
                                print("Opcion fuera de rango")
                                input("Enter to continue")
                            else:
                                opc_borrar=int(opc_borrar)
                                if opc_borrar==tfns.count("#")+1:
                                    flg_borrar_tel=False
                                else:
                                    for i in range(tfns.count("#")):
                                        if i == 0:
                                            inicio3 = 0
                                            final3 = tfns.find("#", inicio3)
                                        else:
                                            inicio3 = final3 + 1
                                            final3 = tfns.find("#", inicio3)
                                        if i+1 == opc_borrar:
                                            if tfns[:inicio3]+tfns[final3+1:]=="":
                                                agenda = agenda[:inicio] + nombre + "*" + direccion + "*" + tfns[:inicio3] +"#"+ tfns[final3 + 1:] + ";" + agenda[final + 1:]
                                            else:
                                                agenda=agenda[:inicio]+nombre+"*"+direccion+"*"+tfns[:inicio3]+tfns[final3+1:]+";"+agenda[final+1:]
                                            print(agenda)
                                            break


                    elif opc_edit == 4:
                        # back
                        flg_edit_contact=False



    while flg_05:
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
                #Search by name
                nom=input("Nombre")
                for i in range(agenda.count(";")):
                    if i == 0:
                        inicio = 0
                        final = agenda.find(";")
                    else:
                        inicio = final + 1
                        final = agenda.find(";", inicio)
                    contacto = agenda[inicio:final]
                    primer_separador = contacto.find("*")
                    segundo_separador = contacto.find("*", primer_separador + 1)
                    nombre = contacto[:primer_separador]
                    direccion = contacto[primer_separador + 1:segundo_separador]
                    telefono = contacto[segundo_separador + 1:]
                    if nom.lower() in nombre.lower():
                        for j in range(telefono.count("#")):
                            if j == 0:
                                inicio2 = 0
                                final2 = telefono.find("#")
                                datos = datos + "{:<20}{:<20}{:>20}\n".format(nombre, direccion, telefono[inicio2:final2])
                            else:
                                inicio2 = final2 + 1
                                final2 = telefono.find("#", inicio2)
                                datos = datos + "{:>60}\n".format(telefono[inicio2:final2])
                        datos = datos + "-" * 60 + "\n"
                print(datos)
                datos = ""


            elif opc == 2:
                #Search from direction
                print("")

            elif opc == 3:
                #Search by num
                print("")

            elif opc==4:
                #Back
                flg_00 = True
                flg_05 = False






