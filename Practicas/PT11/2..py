salir=False
while not salir:
    contra=input("Introduce una contraseña")
    min = False
    mayus = False
    num=False
    alph=False
    space=False
    if len(contra)<8:
        print("La contrasenya ha de tenir un mínim de 8 caràcters.")
    else:
        for i in contra:
            if i.islower():
                min=True
            if i.isupper():
                mayus=True
            if i.isnumeric():
                num=True
            if not i.isalnum():
                alph=True
            if not i.isspace():
                space=True
        if not min:
            print("Ha de contenir una minuscula")
        elif not mayus:
            print("Ha de contenir una mayuscula")
        elif not num:
            print("Ha de contenir un numero")
        elif not alph:
            print("Ha de contenir un no alphanumerico")
        elif not space:
            print("La contrasenya no pot contenir espais en banc")
        else:
            salir=True
            print("Contrasenya correcta")
        input("")

