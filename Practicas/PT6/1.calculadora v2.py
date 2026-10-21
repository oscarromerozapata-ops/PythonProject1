menu = ("Calculadora\n" +
        "Menu Principal\n" +
        "\n" +
        "1 - Sumar\n" +
        "2 - Restar\n" +
        "3 - Multiplicar\n" +
        "4 - Dividir\n" +
        "0 - Sortir\n")

salir= False
while not salir:
    print(menu)
    opcio =input("Opció:")
    if not opcio.isdigit():
        print("Opció no numerica")
        input("Enter to continue")
    elif int(opcio)<0 or int(opcio)>4:
        print("Opció fuera de rango")
        input("Enter to continue")
    else:
        opcio=int(opcio)

        n2 = int(n2)
        if opcio == 1:
            n1 = input("Introdueix un numero")
            while not n1.isdigit():
                print("No has introducido un número")
                input("Enter to continue")
                n1 = input("Introdueix un numero")
            n1 = int(n1)
            n2 = input("Introdueix un numero")
            while not n2.isdigit():
                print("No has introducido un número")
                input("Enter to continue")
                n2 = input("Introdueix un numero")
            res = n1 + n2
            print("Resultat:", res)
            input("Enter to continue")
        if opcio == 2:
            n1 = input("Introdueix un numero")
            while not n1.isdigit():
                print("No has introducido un número")
                input("Enter to continue")
                n1 = input("Introdueix un numero")
            n1 = int(n1)
            n2 = input("Introdueix un numero")
            while not n2.isdigit():
                print("No has introducido un número")
                input("Enter to continue")
                n2 = input("Introdueix un numero")
            res = n1 - n2
            print("Resultat:", res)
            input("Enter to continue")
        if opcio == 3:
            n1 = input("Introdueix un numero")
            while not n1.isdigit():
                print("No has introducido un número")
                input("Enter to continue")
                n1 = input("Introdueix un numero")
            n1 = int(n1)
            n2 = input("Introdueix un numero")
            while not n2.isdigit():
                print("No has introducido un número")
                input("Enter to continue")
                n2 = input("Introdueix un numero")
            res = n1 * n2
            print("Resultat:", res)
            input("Enter to continue")
        if opcio == 4:
            n1 = input("Introdueix un numero")
            while not n1.isdigit():
                print("No has introducido un número")
                input("Enter to continue")
                n1 = input("Introdueix un numero")
            n1 = int(n1)
            n2 = input("Introdueix un numero")
            while not n2.isdigit() or int(n2) == 0:
                if n2.isdigit():
                    print("no puedes dividir por 0")
                else:
                    print("No has introducido un número")
                input("Enter to continue")
            res = n1 / n2
            print("Resultat:", res)
            input("Enter to continue")


