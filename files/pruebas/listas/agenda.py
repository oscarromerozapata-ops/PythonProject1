menu00 = "my agenda".center(40,"*")+"\n" + "1)View Agenda\n2)New Contact\n3)Edit\n4)Delete Contact\n5)Search\n6)Exit"
menu03 = "1)Edit Address\n2)Edit Tfn\n3)Go Back"
menu032 = "1)Add Tfn\n2)Del Tfn\n3)Go Back"
menu05 = "my agenda".center(40,"*") + "\n" +"1)Search By Name\n2)Search By Tfn\n3)Go Back"
cabecera_tabla = "Agenda".center(70,"=")+"\n"+"{:30}{:20}{:>20}\n".format("Name","Address","Tfn") + "="*70+"\n"
flg_00 = True
flg_03 = False
flg_04 = False
flg_05 = False


salir = False
while not salir:
    while flg_00:
        print(menu00)
        opc = input("Option:\n")
        if not opc.isdigit():
            print("Non-Numeric Option ")
            input("Enter to continue")
        elif not int(opc)  in range(1,6):
            print("Option Out Of Range")
            input("Enter to continue")
        else:
            opc = int(opc)
            # ver agenda
            #print("Mostramos agenda = ",agenda)
            if opc == 1:
                datos = ""

                print(cabecera_tabla + datos)
                input("Enter To Continue")
            # nuevo contacto
            if opc == 2:
                print("New Contact")
            # edit
            if opc == 3:
                flg_00 = False
                flg_03 = True
            # delete
            if opc == 4:
                flg_00 = False
                flg_04 = True
            # search
            if opc == 5:
                flg_00 = False
                flg_05 = True
            # exit
            if opc == 6:
                flg_00 = False
                salir = True

            # delete
            while flg_04:
                menu = "Delete Contact".center(40, "*") + "\n"


                print(menu)
                opc = input("Option:\n")
                if not opc.isdigit():
                    print("Non-Numeric Option ")
                    input("Enter to continue")
                elif not int(opc)  in range(1, agenda.count(";")+2):
                    print("Option Out Of Range")
                    input("Enter to continue")
                else:
                    opc = int(opc)
                    # if opc == agenda.count(";")+1:
                    #     flg_00 = True
                    #     flg_04 = False
                    # else:


            # Find
            while flg_05:
                print(menu05)
                opc = input("Option:\n")
                if not opc.isdigit():
                    print("Non-Numeric Option ")
                    input("Enter to continue")
                elif not int(opc) in range(1, 4):
                    print("Option Out Of Range")
                    input("Enter to continue")
                else:
                    opc = int(opc)
                    if opc == 3:
                        flg_05 = False
                        flg_00 = True
                    if opc == 1:
                        datos = ""
                        cadena_buscar = input("Nombre a Buscar\n")

                        print(cabecera_tabla + datos)
                        input("Enter To Continue")
                    if opc == 2:
                        datos = ""
                        tfn_buscar = input("Tfn a buscar")


                        input("Enter To Continue")

            # Editar
            while flg_03:
                menu = "Edit Contact".center(40, "*") + "\n"

                #menu = menu + str(agenda.count(";") + 1) + ")Go Back"
                print(menu)
                opc = input("Option:\n")
                if not opc.isdigit():
                    print("Non-Numeric Option ")
                    input("Enter to continue")
                # elif not int(opc) in range(1, agenda.count(";") + 2):
                #     print("Option Out Of Range")
                #     input("Enter to continue")
                else:
                    opc = int(opc)

                    menu_editar_contacto = "1)Edit Address\n2)Add Tfn\n3)Del Tfn\n4)Exit"
                    flg_edit_contact = True
                    while flg_edit_contact:
                        print(menu_editar_contacto)
                        opc = input("Option:\n")
                        if not opc.isdigit():
                            print("Non-Numeric Option ")
                            input("Enter to continue")
                        elif not int(opc) in range(1, 5):
                            print("Option Out Of Range")
                            input("Enter to continue")
                        else:
                            print("Editar")