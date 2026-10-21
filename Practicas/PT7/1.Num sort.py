#Dissenya un programa que calculi el número de la sort d’una persona a partir de la seua data
#de naixement (dia, mes i any), la qual es proporcionarà com dada al programa com un únic
#número en el format ddmmaaaa. Si la dada de naixement introduïda no és correcta, el
#programa la tornarà a demanar tantes vegades com sigui necessari. El número de la sort és el
#que resulta de reduir a un únic dígit els dígits de la data de naixement.
#Per fer això, es comença sumant els dígits de la data de naixement, es continua sumant cada
#vegada els dígits resultants de la suma anterior, i s’acaba a l’obtenir un sol dígit com resultat
#d’una suma.
#Per exemple: Si la dada de naixement és el 29 de setembre de 1981 (29091981), el
#número de la sort és el 3, que s’obté com resultat de realitzar les sumes:
#2+9+0+9+1+9+8+1=39, 3+9=12 i 1+2=3.
#Pista: Per al càlcul dels dígits pots agafar el residu de les divisions successives entre 10
#del número corresponent a la data
sort=0
salida= False
while not salida:
    dada = input("Introduce tu fecha de nacimiento ddmmaaaa")
    if not dada.isdigit():
        print("Opción no numérica")
        input("Enter to continue")
    else:
        num=int(dada)
        print("a")
        for i in dada:
            sort=sort+num%10
            num=num//10
            salida=True
print(sort,num)