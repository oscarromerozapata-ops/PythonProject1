salir=False

while not salir:
    nom = input("Introduce un nombre")
    if len(nom)<6 :
        print("El nom de usuari ha de contenir almenys 6 caràcters ")
    elif len(nom)>12:
        print("El nom de usuari no pot contenir més de 12 caràcters ")
    elif not nom.isalnum():
        print("El nom d'usuari pot contenir només lletres i números")
    else:
        print("Nom d'usuari correcte")