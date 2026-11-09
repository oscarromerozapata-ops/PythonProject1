agenda="Pedro*Balmes 27*111111111#333425325#+4534553453#;Jacinta*Ardur 32*333333333#657483746#;Andres*Arriba 1**444444444#374658365#;Anabel*Derecha 3**222222222#465768347#;"
contacto=""
datos=""
menu00="1)View contacts\n2)New contact\n3)Edit contact\n4)Remove contact\n5)Search contact\n6)salir"
menu03="1)Edit direction\n2)Add tfn\n3)Remove tfn\n4)back"
menu05="1)Search by name\n2)Search from direction\n3)Search by num\n4)back"
salir=False
flg_00=True
flg_03=False
flg_04=False

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
                datos=datos+"{:<20}{:<20}{:>20}\n".format(nombre,direccion,tfns[inicio2:final2])
                datos=datos+"{:>60}\n".format(tfns[inicio2:final2])
                datos=datos+"-"*60+"\n"
                print(datos)
            elif opc==2:
                #New contact
                nombre=input("nombre")
                direccion=input("direccion")
                numero=input("numero")
                contacto=nombre+"*"+direccion+"*"+numero+"#;"
            elif opc==3:
                #Edit contact
                flg_00=False
                flg_03=True
            elif opc==4:
                #Remove contact
                print("Remove contact")
            elif opc==5:
                #Search contact
                flg_05=True
                flg_00=False
            elif opc==6:
                salir=True
                flg_00 = False
    while flg_03:
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
                #Edit direction
                print("")

            elif opc==2:
                #Add tfn
                print("")

            elif opc==3:
                #Remove tfn
                print("")
            elif opc==4:
                #back
                flg_00=True
                flg_03=False
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
                print("")

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






