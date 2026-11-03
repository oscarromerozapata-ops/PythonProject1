agenda = [
    ["Alberto Castaño Sanchez", "Balmes 27 1º2º ", ["666344551","777000000"]],
    ["Enrique Casado Ruiz" , "Rocafort 234 5º1º" ,["674343536","937182323","345343434"]],
    ["Esther Flores Ruiz", "Numancia 345 10º A", ["657876543"]],
    ["Maria Lopez Vallejo", "Bonavista 43 3º3º" , ["667344556","937249898"]]
]
cabecera="Agenda".center(70,"=")+"\n"+"{:30}{:20}{:>20}\n".format("Nombre","Direccion","Numero")+"="*70+"\n"
datos=""
menu00="1)View contacts\n2)New contact\n3)Edit contact\n4)Remove contact\n5)Search contact\n6)salir"
menu03="1)Edit direction\n2)Add tfn\n3)Remove tfn\n4)back"
menu05="1)Search by name\n2)Search from direction\n3)Search by num\n4)back"
salir=False
flg_00=True
flg_03=False
flg_04=False
flg_05=False
flg_edit_contact=False
flg_add_num=False
datos=""
while not salir:
    while flg_00:
        print(menu00)
        opc = input("Option:\n")
        if not opc.isdigit():
            print("Non-Numeric Option ")
            input("Enter to continue")
        elif not int(opc)  in range(1,7):
            print("Option Out Of Range")
            input("Enter to continue")
        else:
            opc = int(opc)
            # ver agenda
            #print("Mostramos agenda = ",agenda)
            if opc == 1:
                for i in range (len(agenda)):
                    nom=agenda[i][0]
                    direccion=agenda[i][1]
                    num=str(agenda[i][2])
                    for j in range (len(agenda[i][2])):
                        if j==0:
                            datos = datos + "{:30}{:20}{:>20}\n".format(nom, direccion, agenda[i][2][j])
                        else:
                            datos = datos + "{:30}{:20}{:>20}\n".format("", "", agenda[i][2][j])
                    datos=datos+"-"*70+"\n"
                print(cabecera+datos)
                input("Enter to continue")
                datos=""
            if opc == 2:
                nuevo_contacto=["Bernardo Simon Lopez","Sepulveda 234 1º 2º",["123123123","456456456"]]
                longitud_inicial=len(agenda)
                for i in range (len(agenda)):
                    nom=agenda[i][0]
                    direccion=agenda[i][1]
                    num=agenda[i][2]
                    if nuevo_contacto[0]< nom:

                #         agenda=agenda[:i]+nuevo_contacto+agenda[i+1:]
                #         break
                # print (agenda)
                        agenda.insert(i,nuevo_contacto)
                    break
                if len(agenda)==longitud_inicial:
                    agenda.append(nuevo_contacto)
            if opc==3:
                flg_00 = False
                flg_03 = True
            if opc ==4:
                flg_00=False
                flg_04=True
            if opc==5:
                flg_00=False
                flg_05=True
            if opc==6:
                flg_00=False
                salir=True
    while flg_03:
        for i in range(len(agenda)):
            nom = agenda[i][0]
            direccion = agenda[i][1]
            num = str(agenda[i][2])
            for j in range(len(agenda[i][2])):
                if j == 0:
                    datos = datos + "{}{:2}{:30}{:20}{:>17}\n".format(i + 1, ")", nom, direccion,
                                                                      agenda[i][2][j])
                else:
                    datos = datos + "{:30}{:20}{:>20}\n".format("", "", agenda[i][2][j])
            datos = datos + "-" * 70 + "\n"
        datos = datos + str(i + 2) + ")Salir\n"
        print(cabecera + datos)
        datos = ""
        opc_edit = input("Opción")
        if not opc_edit.isdigit():
            print("Non-Numeric Option ")
            input("Enter to continue")
        elif int(opc_edit) in (0, len(agenda) + 2):
            print("Option Out Of Range")
            input("Enter to continue")
        elif int(opc_edit) == len(agenda) + 1:
            flg_03=False
            flg_00=True
        else:
            flg_edit_contact=True
            opc_edit = int(opc_edit)

        while flg_edit_contact:
            print(menu03)
            opc = input("Option:\n")
            if not opc.isdigit():
                print("Non-Numeric Option ")
                input("Enter to continue")
            elif not int(opc) in range(1, 5):
                print("Option Out Of Range")
                input("Enter to continue")
            else:
                opc = int(opc)
                if opc == 1:
                    nueva_direccion = "patata"
                    agenda[opc - 1][1] = nueva_direccion
                if opc == 2:
                    nuevo_tel = "333333333"
                    agenda[opc_edit - 1][2].append(nuevo_tel)
                if opc == 3:
                    tfns_originales=agenda[opc_edit-1][2]

                    flg_del_tfn=True
                    while flg_del_tfn:
                        menu_borrar_tfns = "Delete tfn".center(50, "*") + "\n"
                        for j in range(len(tfns_originales)):
                            menu_borrar_tfns = menu_borrar_tfns + str(j + 1) + ")" + tfns_originales[j] + "\n"
                        menu_borrar_tfns = menu_borrar_tfns + str(len(tfns_originales) + 1) + ")Back" + "\n"
                        print(menu_borrar_tfns)
                        opc_del_tfn = input("Option:\n")
                        if not opc_del_tfn.isdigit():
                            print("Non-Numeric Option ")
                            input("Enter to continue")
                        elif not int(opc_del_tfn) in range(1, len(tfns_originales)+2):
                            print("Option Out Of Range")
                            input("Enter to continue")
                        else:
                            opc_del_tfn = int(opc_del_tfn)
                            if opc_del_tfn-1 == len(tfns_originales):
                                flg_del_tfn = False
                            else:
                                tfns_originales.pop(opc_del_tfn-1)
                if opc == 4:
                    flg_edit_contact=False
    while flg_04:
        menu = "Delete contact".center(40, "*") + "\n"
        for i in range(len(agenda)):
            nom = agenda[i][0]
            direccion = agenda[i][1]
            num = str(agenda[i][2])
            menu = menu + str(i + 1) + ")" + nom + ";" + direccion + "\n"
        menu = menu + str(len(agenda) + 1) + ")Back" + "\n"

        print(menu)
        opc = input("Option:\n")
        if not opc.isdigit():
            print("Non-Numeric Option ")
            input("Enter to continue")
        elif not int(opc) in range(1, len(agenda) + 2):
            print("Option Out Of Range")
            input("Enter to continue")
        else:
            opc = int(opc)
            if opc == len(agenda) + 1:
                flg_00 = True
                flg_04 = False
            else:
                agenda.remove(agenda[opc-1])
                print (agenda)
    while flg_05:
        print(menu05)
        opc = input("Option:\n")
        if not opc.isdigit():
            print("Non-Numeric Option ")
            input("Enter to continue")
        elif not int(opc) in range(1, 5):
            print("Option Out Of Range")
            input("Enter to continue")
        else:
            opc = int(opc)
            if opc==1:
                nombre = input("Nombre:\n")
                for i in range(len(agenda)):
                    nom = agenda[i][0]
                    direccion = agenda[i][1]
                    num = str(agenda[i][2])
                    if nombre.lower() in nom.lower():
                        for j in range(len(agenda[i][2])):
                            if j == 0:
                                datos = datos + "{:30}{:20}{:>20}\n".format(nom, direccion, agenda[i][2][j])
                            else:
                                datos = datos + "{:30}{:20}{:>20}\n".format("", "", agenda[i][2][j])
                        datos = datos + "-" * 70 + "\n"
                print(cabecera + datos)
                input("Enter to continue")
                datos = ""
            if opc==3:
                tel = input("Numero:\n")
                for i in range(len(agenda)):
                    nom = agenda[i][0]
                    direccion = agenda[i][1]
                    num = agenda[i][2]
                    for k in range(len(num)):
                        if tel in num[k]:
                            print("a")
                            for j in range(len(num)):
                                if j == 0:
                                    datos = datos + "{:30}{:20}{:>20}\n".format(nom, direccion, agenda[i][2][j])
                                else:
                                    datos = datos + "{:30}{:20}{:>20}\n".format("", "", agenda[i][2][j])
                            datos = datos + "-" * 70 + "\n"
                            break


                print(cabecera + datos)
                input("Enter to continue")
                datos = ""

            if opc==4:
                flg_05 = False
                flg_00 = True