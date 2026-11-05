agenda="Pedro*Balmes 27*111111111#333425325#+4534553453#;Jacinta*Ardur 32*333333333#657483746#;Andres*Arriba 1**444444444#374658365#;Anabel*Derecha 3**222222222#465768347#;"
menu="1)Edit direction\n2)Add tfn\n3)Remove tfn\n4)back"
flg_menu=True
datos=""
while flg_menu:
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
    opc = input("Option")
    if not opc.isdigit():
        print("Opcion fuera de rango")
        input("Enter to continue")
    elif not int(opc) in range(1, agenda.count(";") + 2):
        print("Opcion fuera de rango")
        input("Enter to continue")
    else:
        opc = int(opc)
        if opc == agenda.count(";")+1:
            flg_03 = False
        else:
            flg_edit_contact=True
            while flg_edit_contact:
                print(menu)
                opc_edit = input("Option")
                if not opc_edit.isdigit():
                    print("Opcion fuera de rango")
                    input("Enter to continue")
                elif not int(opc_edit) in range(1, 5):
                    print("Opcion fuera de rango")
                    input("Enter to continue")
                else:
                    opc_edit = int(opc_edit)
                    if opc_edit ==4:
                        flg_edit_contact = False
                    else:
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
                            if i+1==opc:

                                break

                        if opc_edit==1:
                            #edit direction
                            nueva_direccion = "patata"
                            agenda=agenda[:inicio]+nombre+"*"+nueva_direccion+"*"+telefono+";"+agenda[final+1:]
                        elif opc_edit==2:
                            #add tfns
                            nuevo_tel="696969697"
                            agenda=agenda[:inicio]+nombre+"*"+direccion+"*"+telefono+nuevo_tel+"#;"+agenda[final+1:]
                        elif opc_edit==3:
                            flg_delete_num=True
                            while flg_delete_num:
                                menu_borrar_tel="Delete tel".center(30,"*")+"\n"
                                for i in range(telefono.count("#")):
                                    if i ==0:
                                        inicio3=0
                                        final3=telefono.find("#", inicio3)
                                    else:
                                        inicio3=final3+1
                                        final3=telefono.find("#", inicio3)
                                    menu_borrar_tel=menu_borrar_tel+str(i+1)+")"+telefono[inicio3:final3]+"\n"
                                menu_borrar_tel=menu_borrar_tel+str(i+2)+")Back\n"
                                print(menu_borrar_tel)
                                opc_borrar = input("Option")
                                if not opc_borrar.isdigit():
                                    print("Opcion fuera de rango")
                                    input("Enter to continue")
                                elif not int(opc_borrar) in range(1, telefono.count("#")+2):
                                    print("Opcion fuera de rango")
                                    input("Enter to continue")
                                else:
                                    opc_borrar = int(opc_borrar)
                                    if opc_borrar == telefono.count("#")+1:
                                        flg_delete_num = False
                                    else:
                                        for j in range(telefono.count("#")):
                                            if j == 0:
                                                inicio3 = 0
                                                final3 = telefono.find("#", inicio3)
                                            else:
                                                inicio3 = final3 + 1
                                                final3 = telefono.find("#", inicio3)
                                            if j+1==opc_borrar:
                                                telefono=telefono[:inicio3]+telefono[final3+1:]
                                                print(telefono)
                                                print(agenda)
                                                agenda=agenda[:inicio]+nombre+"*"+direccion+"*"+telefono+";"+agenda[final+1:]
                                                print(agenda)
                                                break
