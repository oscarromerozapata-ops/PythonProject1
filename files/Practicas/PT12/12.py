import math



submenus = {
    "4": ("Primer vector menys segon vector.", "Segon vector menys primer vector."),
    "6": ("Primer vector x segon vector.", "Segon vector x primer vector."),
    "8": ("Longitud del primer vector.", "Longitud del segon vector."),
}

menu00 = "1. Introduir el primer vector\n2. Introduir el segon vector\n3. Calcular la suma\n4. Calcular la diferència\n5. Calcular el producte escalar\n6. Calcular el producte vectorial\n7. Calcular l'angle (en graus) entre ells\n8. Calcular la longitud\n9. Finalitzar"
menu04="1.Primer vector x segon vector.\n2.Segon vector x primer vector."
menu06="1.Primer vector x segon vector.\n2.Segon vector x primer vector."
salir=False
x1=10
y1=10
z1=10
x2=20
y2=20
z2=20
while not salir:
    print(menu00)
    opc=input()
    if not opc.isdigit():
        input("Introduce un numero")
    elif not int(opc) in range(1,10):
        input("Introduce un numero")
    else:
        opc=int(opc)
        if opc==1:
            x1=int(input("Introduce x1"))
            y1=int(input("Introduce y1"))
            z1=int(input("Introduce z1"))
        elif opc==2:
            x2 = int(input("Introduce x2"))
            y2 = int(input("Introduce y2"))
            z2 = int(input("Introduce z2"))
        else:
            if x1==""or y1==""or z1=="" or x2=="" or y2=="" or z2=="":
                input("Introduce un vector")
            else:
                if opc==3:
                    print("Suma",x1+x2,y1+y2,z1+z2)
                elif opc==4:
                    print(menu04)
                    opc=int(input("Opcion"))
                    if opc==1:
                        print("Diferencia ",x1 - x2, y1 - y2, z1-z2)
                    elif opc==2:
                        print("Diferencia ",x2 - x1, y2 - y1, z2 - z1)
                elif opc==5:
                    print("Producte escalar:", x1 * x2 + y1 * y2 + z1 * z2)
                elif opc==6:
                    print(menu06)
                    opc = int(input("Opcion"))
                    if opc == 1:
                        print("Producte vectorial:", y1 * z2 - z1 * y2,z1 * x2 - x1 * z2,x1 * y2 - y1 * x2)
                    elif opc == 2:
                        print("Producte vectorial:",y2 * z1 - z2 * y1, z2 * x1 - x2 * z1, x2 * y1 - y2 * x1)
                elif opc==7:
                    print("Angle", 180/math.pi*math.acos(x1*x2+y1*y2+z1*z2/math.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2)+math.sqrt(x2 ** 2 + y2 ** 2 + z2 ** 2)))
                elif opc==8:
                    print("Longitud ", math.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2))
                elif opc==9:
                    salir=True