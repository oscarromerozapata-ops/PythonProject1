menu00="Menu00\n1)opc1\n2)opc2\n3)salir"
menu01="Menu01\n1)opc1\n2)opc2\n3)back"
menu02="Menu02\n1)opc1\n2)opc2\n3)back"
menu023="Menu023\n1)opc1\n2)opc2\n3)opc3\n4)back"
flg_00=True
flg_01=False
flg_02=False
flg_023=False
salir=False
while not salir:
    while flg_00:
        print(menu00)
        opc=input("opc:\n")
        if not opc.isdigit():
            print("Opción no numérica")
            input("Enter to continue")
        elif int(opc)<1 or int(opc)>3:
            print("Opción fuera de rango")
            input("Enter ro continue")
        else:
            opc=int(opc)
            if opc==1:
                flg_00=False
                flg_01=True
                print("Vamos al menú 01")
            if opc==2:
                flg_00 = False
                flg_02 = True
                print("Vamos al menú 02")
            if opc==3:
                print("Salir")
                salir=True
    while flg_01:
        print(menu01)
        opc=input("opc:\n")
        if not opc.isdigit():
            print("Opción no numérica")
            input("Enter to continue")
        elif int(opc)<1 or int(opc)>3:
            print("Opción fuera de rango")
            input("Enter ro continue")
        else:
            opc=int(opc)
            if opc==1:
                print("Vamos al menú 011")
            if opc==2:
                print("Vamos al menú 012")
            if opc==3:
                flg_01=False
                flg_00=True
    while flg_02:
        print(menu02)
        opc=input("opc:\n")
        if not opc.isdigit():
            print("Opción no numérica")
            input("Enter to continue")
        elif int(opc)<1 or int(opc)>4:
            print("Opción fuera de rango")
            input("Enter ro continue")
        else:
            opc=int(opc)
            if opc==1:
                print("Vamos al menú 021")
            if opc==2:
                print("Vamos al menú 022")
            if opc == 3:
                print("Vamos al menú 023")
                flg_02 = False
                flg_023 = True
            if opc==4:
                flg_02=False
                flg_00=True
    while flg_023:
        print(menu023)
        opc = input("opc:\n")
        if not opc.isdigit():
            print("Opción no numérica")
            input("Enter to continue")
        elif int(opc) < 1 or int(opc) > 3:
            print("Opción fuera de rango")
            input("Enter ro continue")
        else:
            opc = int(opc)
            if opc == 1:
                print("Vamos al menú 021")
            if opc == 2:
                print("Vamos al menú 022")
            if opc == 3:
                flg_023 = False
                flg_02 = True