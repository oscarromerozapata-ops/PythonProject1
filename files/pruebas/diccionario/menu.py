letrasDni = ('T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E')
usuario1 = {"nombre":"Pedro Javier Morales",  "direccion": "Flores 36 8º 2º", "tfn":["+0034345345345"],"compras":[1234,423,23]}
usuario2 = {"nombre":"Maite Lopez Miravet", "direccion":"Balmes 31 1º 2º","tfn":["+0034234234235","+0034239999235"],"compras":[12344]}
usuario3 = {"nombre":"Marta Garcia Suarez",  "direccion":"Valencia 21 3º 1º","tfn": ["+0075766576575"],"compras":[34,423,23,6]}
usuarios = {"47474747X":usuario1,"24536425T":usuario2,"76767676H":usuario3}
cabecera="{:12}{:25}{:20}{:20}{:15}\n".format("DNI","Nombre","Direccion","Tfn","Total Compras")

menu00="Welcome to the User Management Program".center(50,"*")+"\n\n1)Create User\n2)Modify User\n3)Show Users\n4)Find User\n5)List Users\n6)Exit"
menu04="1)Find by DNI\n2)Find by Name\n3)Go Back"
menu05="1)List Users by DNI\n2)List Users by Name\n3)List Users by Address\n4)List Users by Total Purchase\n5)Go Back"
flg_00=True
flg_05=False
flg_04=False
salir=False
while not salir:
    while flg_00:
        print(menu00)
        opc=input("Option:")
        if not opc.isdigit():
            print("Opcion no numerica")
            input("Enter to continue")
        elif not int(opc) in range (1,7):
            print("Opcion no valida")
            input("Enter to continue")
        else:
            opc=int(opc)
            if opc==1:
                print("Create")
            elif opc==2:
                print("Modify")
            elif opc==3:
                datos = ""

                for dni in usuarios:
                    suma_compras = 0
                    for compra in usuarios[dni]["compras"]:
                        suma_compras += compra
                    datos = datos + "{:12}{:25}{:20}{:20}{:15}\n".format(dni, usuarios[dni]["nombre"],
                                                                         usuarios[dni]["direccion"],
                                                                         usuarios[dni]["tfn"][0],
                                                                         str(suma_compras))
                    str(suma_compras)
                    if len(usuarios[dni]["tfn"]) > 1:
                        for i in range(1, len(usuarios[dni]["tfn"])):
                            datos = datos + "{:12}{:25}{:20}{:20}{:25}{:15}\n".format("", "", "",
                                                                                      usuarios[dni]["tfn"][
                                                                                          i], "", "")
                    datos = datos + "*" * 90 + "\n"
                print(cabecera + datos)
            elif opc==4:
                flg_04 = True
                while flg_04:
                    print(menu04)
                    opc = input("Option:")
                    if not opc.isdigit():
                        print("Opcion no numerica")
                        input("Enter to continue")
                    elif not int(opc) in range(1, 4):
                        print("Opcion no valida")
                        input("Enter to continue")
                    else:
                        opc = int(opc)
                        if opc==1:
                            datos = ""
                            menu_buscar_dni="Buscar DNI".center(12,"*")+"\n"
                            contador=0
                            for dni in usuarios:
                                contador+=1
                                menu_buscar_dni=menu_buscar_dni+"{}) {}\n".format(contador,dni)
                            menu_buscar_dni=menu_buscar_dni+"{}) {}".format(contador+1,"Go Back")
                            print(menu_buscar_dni)
                            opc = input("Option:")
                            if not opc.isdigit():
                                print("Opcion no numerica")
                                input("Enter to continue")
                            elif not int(opc) in range(1, contador+1):
                                print("Opcion no valida")
                                input("Enter to continue")
                            else:
                                opc = int(opc)
                                if opc==contador+1:
                                    flg_04=False
                                else:
                                    datos = ""
                                    for dni in usuarios:
                                        suma_compras = 0
                                        for compra in usuarios[dni]["compras"]:
                                            suma_compras += compra
                                        datos = datos + "{:12}{:25}{:20}{:20}{:15}\n".format(dni, usuarios[dni]["nombre"],
                                                                                             usuarios[dni]["direccion"],
                                                                                             usuarios[dni]["tfn"][0],
                                                                                             str(suma_compras))
                                        str(suma_compras)
                                        if len(usuarios[dni]["tfn"]) > 1:
                                            for i in range(1, len(usuarios[dni]["tfn"])):
                                                datos = datos + "{:12}{:25}{:20}{:20}{:25}{:15}\n".format("", "", "",
                                                                                                          usuarios[dni]["tfn"][
                                                                                                              i], "", "")
                                        datos = datos + "*" * 90 + "\n"
                                print(cabecera + datos)
                        elif opc==3:
                            flg_04=False
            elif opc==5:
                #menu list users
                flg_05=True
                while flg_05:
                    print(menu05)
                    opc=input("Option:")
                    if not opc.isdigit():
                        print("Opcion no numerica")
                        input("Enter to continue")
                    elif not int(opc) in range (1,6):
                        print("Opcion no valida")
                        input("Enter to continue")
                    else:
                        opc=int(opc)
                        if opc==1:
                            #print("list users bby dni")
                            lista_dni=list(usuarios.keys())
                            for pasada in range(len(lista_dni)-1):
                                for i in range (len(lista_dni)-1-pasada):
                                    if lista_dni[i]>lista_dni[i+1]:
                                        aux=lista_dni[i]
                                        lista_dni[i]=lista_dni[i+1]
                                        lista_dni[i+1]=aux
                            print(lista_dni)
                            datos=""
                            for dni in lista_dni:
                                suma_compras = 0
                                for compra in usuarios[dni]["compras"]:
                                    suma_compras += compra
                                datos = datos + "{:12}{:25}{:20}{:20}{:15}\n".format(dni, usuarios[dni]["nombre"],usuarios[dni]["direccion"],usuarios[dni]["tfn"][0],str(suma_compras))
                                str(suma_compras)
                                if len(usuarios[dni]["tfn"]) > 1:
                                    for i in range(1, len(usuarios[dni]["tfn"])):
                                        datos = datos + "{:12}{:25}{:20}{:20}{:25}{:15}\n".format("", "", "",usuarios[dni]["tfn"][i], "", "")
                                datos = datos + "*" * 90 + "\n"
                            print(cabecera + datos)
                        elif opc==2:
                            #print("list users by name")
                            lista_dni = list(usuarios.keys())
                            for pasada in range(len(lista_dni) - 1):
                                for i in range(len(lista_dni) - 1 - pasada):
                                    if usuarios[lista_dni[i]]["nombre"]>usuarios[lista_dni[i+1]]["nombre"]:
                                        aux = lista_dni[i]
                                        lista_dni[i] = lista_dni[i + 1]
                                        lista_dni[i + 1] = aux
                            print(lista_dni)
                            datos = ""
                            for dni in lista_dni:
                                suma_compras = 0
                                for compra in usuarios[dni]["compras"]:
                                    suma_compras += compra
                                datos = datos + "{:12}{:25}{:20}{:20}{:15}\n".format(dni, usuarios[dni]["nombre"],
                                                                                     usuarios[dni]["direccion"],
                                                                                     usuarios[dni]["tfn"][0],
                                                                                     str(suma_compras))
                                str(suma_compras)
                                if len(usuarios[dni]["tfn"]) > 1:
                                    for i in range(1, len(usuarios[dni]["tfn"])):
                                        datos = datos + "{:12}{:25}{:20}{:20}{:25}{:15}\n".format("", "", "",
                                                                                                  usuarios[dni]["tfn"][
                                                                                                      i], "", "")
                                datos = datos + "*" * 90 + "\n"
                            print(cabecera + datos)

                        elif opc==3:
                            lista_dni = list(usuarios.keys())
                            for pasada in range(len(lista_dni) - 1):
                                for i in range(len(lista_dni) - 1 - pasada):
                                    if usuarios[lista_dni[i]]["direccion"] > usuarios[lista_dni[i + 1]]["direccion"]:
                                        aux = lista_dni[i]
                                        lista_dni[i] = lista_dni[i + 1]
                                        lista_dni[i + 1] = aux
                            print(lista_dni)
                            datos = ""
                            for dni in lista_dni:
                                suma_compras = 0
                                for compra in usuarios[dni]["compras"]:
                                    suma_compras += compra
                                datos = datos + "{:12}{:25}{:20}{:20}{:15}\n".format(dni, usuarios[dni]["nombre"],
                                                                                     usuarios[dni]["direccion"],
                                                                                     usuarios[dni]["tfn"][0],
                                                                                     str(suma_compras))
                                str(suma_compras)
                                if len(usuarios[dni]["tfn"]) > 1:
                                    for i in range(1, len(usuarios[dni]["tfn"])):
                                        datos = datos + "{:12}{:25}{:20}{:20}{:25}{:15}\n".format("", "", "",
                                                                                                  usuarios[dni]["tfn"][
                                                                                                      i], "", "")
                                datos = datos + "*" * 90 + "\n"
                            print(cabecera + datos)
                        elif opc==4:
                            lista_dni = list(usuarios.keys())
                            diccionario_compras={}
                            for dni in lista_dni:
                                diccionario_compras[dni] = 0
                                for compra in usuarios[dni]["compras"]:
                                    diccionario_compras[dni]=diccionario_compras[dni]+compra

                            for pasadas in range(len(lista_dni) - 1):
                                for i in range(len(lista_dni) - 1 - pasadas):
                                    if diccionario_compras[lista_dni[i]] < diccionario_compras[lista_dni[i + 1]]:
                                        aux = lista_dni[i]
                                        lista_dni[i] = lista_dni[i + 1]
                                        lista_dni[i + 1] = aux

                            datos = ""

                            for dni in lista_dni:
                                suma_compras = 0
                                for compra in usuarios[dni]["compras"]:
                                    suma_compras += compra
                                datos = datos + "{:12}{:25}{:20}{:20}{:15}\n".format(dni, usuarios[dni]["nombre"],
                                                                                     usuarios[dni]["direccion"],
                                                                                     usuarios[dni]["tfn"][0],
                                                                                     str(suma_compras))
                                str(suma_compras)
                                if len(usuarios[dni]["tfn"]) > 1:
                                    for i in range(1, len(usuarios[dni]["tfn"])):
                                        datos = datos + "{:12}{:25}{:20}{:20}{:25}{:15}\n".format("", "", "",
                                                                                                  usuarios[dni]["tfn"][
                                                                                                      i], "", "")
                                datos = datos + "*" * 90 + "\n"
                            print(cabecera + datos)
                        elif opc==5:
                            flg_05=False
            elif opc==6:
                #exit
                flg_00=False
                salir=True