menu00="Menu00".center(20,"*")+"\n1)menu01\n2)menu02\n3)salir"
menu01="Menu01".center(20,"*")+"\n1)menu011\n2)menu012\n3)back"
menu011="Menu011".center(20,"*")+"\n1)menu0111\n2)menu0112\n3)back"
menu0111="Menu0111".center(20,"*")+"\n1)menu01111\n2)menu01112\n3)back"
menu0112="Menu0112".center(20,"*")+"\n1)menu01121\n2)menu01122\n3)back"
menu012="Menu012".center(20,"*")+"\n1)menu0121\n2)menu0122\n3)back"
menu0121="Menu0121".center(20,"*")+"\n1)menu01211\n2)menu01212\n3)back"
menu0122="Menu0122".center(20,"*")+"\n1)menu01221\n2)menu01222\n3)back"
menu02="Menu02".center(20,"*")+"\n1)menu021\n2)menu022\n3)back"
menu021="Menu021".center(20,"*")+"\n1)menu0211\n2)menu0212\n3)back"
menu0211="Menu0211".center(20,"*")+"\n1)menu02111\n2)menu02112\n3)back"
menu0212="Menu0212".center(20,"*")+"\n1)menu02121\n2)menu02122\n3)back"
menu022="Menu022".center(20,"*")+"\n1)menu0221\n2)menu0222\n3)back"
menu0221="Menu0221".center(20,"*")+"\n1)menu02211\n2)menu02212\n3)back"
menu0222="Menu0222".center(20,"*")+"\n1)menu02221\n2)menu02222\n3)back"
flg_00=True
flg_01=False
flg_011=False
flg_0111=False
flg_0112=False
flg_012=False
flg_0121=False
flg_0122=False
flg_02=False
flg_021=False
flg_0211=False
flg_0212=False
flg_022=False
flg_0221=False
flg_0222=False
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
                print("Saliendo")
                flg_00 = False
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
                flg_01=False
                flg_011 = True
                print("Vamos al menú 011")
            if opc==2:
                flg_01 = False
                flg_012 = True
                print("Vamos al menú 012")
            if opc==3:
                flg_01=False
                flg_00=True
    while flg_011:
        print(menu011)
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
                flg_011 = False
                flg_0111 = True
                print("Vamos al menú 0111")
            if opc==2:
                flg_011 = False
                flg_0112 = True
                print("Vamos al menú 0112")
            if opc==3:
                flg_011=False
                flg_01=True
    while flg_0111:
        print(menu0111)
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
                print("Vamos al menú 01111")
            if opc==2:
                print("Vamos al menú 01112")
            if opc==3:
                flg_0111=False
                flg_011=True
    while flg_0112:
        print(menu0112)
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
                print("Vamos al menú 01121")
            if opc==2:
                print("Vamos al menú 01122")
            if opc==3:
                flg_0112=False
                flg_011=True
    while flg_012:
        print(menu012)
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
                flg_012 = False
                flg_0121 = True
                print("Vamos al menú 0121")
            if opc==2:
                flg_012 = False
                flg_0122 = True
                print("Vamos al menú 0122")
            if opc==3:
                flg_012=False
                flg_01=True
    while flg_0121:
        print(menu0121)
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
                print("Vamos al menú 01211")
            if opc==2:
                print("Vamos al menú 01212")
            if opc==3:
                flg_0121=False
                flg_012=True
    while flg_0122:
        print(menu0122)
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
                print("Vamos al menú 01221")
            if opc==2:
                print("Vamos al menú 01222")
            if opc==3:
                flg_0122=False
                flg_012=True
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
                flg_02=False
                flg_021=True
                print("Vamos al menú 021")
            if opc==2:
                flg_02=False
                flg_022=True
                print("Vamos al menú 022")
            if opc==3:
                flg_02=False
                flg_00=True
    while flg_021:
        print(menu021)
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
                flg_021 = False
                flg_0211 = True
                print("Vamos al menú 0211")
            if opc==2:
                flg_021 = False
                flg_0212 = True
                print("Vamos al menú 0212")
            if opc==3:
                flg_021=False
                flg_02=True
    while flg_0211:
        print(menu0211)
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
                print("Vamos al menú 02111")
            if opc==2:
                print("Vamos al menú 02112")
            if opc==3:
                flg_0211=False
                flg_021=True
    while flg_0212:
        print(menu0212)
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
                print("Vamos al menú 02121")
            if opc==2:
                print("Vamos al menú 02122")
            if opc==3:
                flg_0212=False
                flg_021=True
    while flg_022:
        print(menu022)
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
                flg_022 = False
                flg_0221 = True
                print("Vamos al menú 0221")
            if opc==2:
                flg_022 = False
                flg_0222 = True
                print("Vamos al menú 0222")
            if opc==3:
                flg_022=False
                flg_02=True
    while flg_0221:
        print(menu0221)
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
                print("Vamos al menú 02211")
            if opc==2:
                print("Vamos al menú 02212")
            if opc==3:
                flg_0221=False
                flg_022=True
    while flg_0222:
        print(menu0222)
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
                print("Vamos al menú 02221")
            if opc==2:
                print("Vamos al menú 02222")
            if opc==3:
                flg_0222=False
                flg_022=True