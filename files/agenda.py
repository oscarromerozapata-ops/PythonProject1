tabla="Agenda".center(40,"*")+"\n"+"{:20}{:>20}\n".format("Nombre","tel")+"*"*40+"\n"
selec="introduce un número\n1)Agenda\n2)Agregar numero\n3)Salir\n"
salir=False
datos=""
while not salir:
    opc=input(selec)
    if not opc.isdigit()or int(opc)>4 or int(opc)<=0:
        print("Error")
        input("Enter to continue")
    else:
        opc=int(opc)
        if opc==1:
            print(tabla+datos)
            input("Enter to continue")
        elif opc==2:
            nom=input("Introduce el nombre")
            numero=input("Escribe el numero")
            while not numero.isdigit():
                print("Telefono no valido")
                numero = input("Escribe el numero")
            print("Quieres guardar a {} con el numero {} en la agenda?".format(nom,numero))
            resp=input("(S/N)")
            if resp=="S":
                datos+="{:20}{:>20}\n".format(nom,numero)
        elif opc==3:
            salir=True