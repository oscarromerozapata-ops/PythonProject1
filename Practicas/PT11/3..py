nombre=False

while not nombre:
    nom = input("Introduce un nombre")
    if len(nom)<6 :
        print("El nom de usuari ha de contenir almenys 6 caràcters ")
    elif len(nom)>12:
        print("El nom de usuari no pot contenir més de 12 caràcters ")
    elif not nom.isalnum():
        print("El nom d'usuari pot contenir només lletres i números")
    else:
        print("Nom d'usuari correcte")
        nombre=True
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
