import random
menu00="1)Jugador1\n2)Jugador2\n3)jugar\n4)salir"
resp=""
j1 = ""
j2 = ""
while not resp==4:
    print(menu00)
    resp=input("Opción: ")
    if not resp.isdigit():
        print("Error vuelve a intentar")
    else:
        resp=int(resp)
        if resp>4 or resp<1:
            print("numero fuera de rango")
        else:
            resp= int(resp)
            if resp==1:
                j1=input("Nombre jugador 1")
            if resp==2:
                j2=input("nombre jugador 2")
            if resp==3:
                if j1=="" or j2=="":
                    print("Falta el nombre del jugador")
                else:
                    puntos_j1=0
                    puntos_j2=0
                    while puntos_j1<3 and puntos_j2<3:
                        dado1= random.randrange(1,4)
                        dado2= random.randrange(1,4)
                        if dado1==1:
                            print("jugador {} saca piedra".format(j1))
                        elif dado1==2:
                            print("jugador {} saca papel".format(j1))
                        elif dado1==3:
                            print("jugador {} saca tijera".format(j1))
                        if dado2==1:
                            print("jugador {} saca piedra".format(j2))
                        elif dado2==2:
                            print("jugador {} saca papel".format(j2))
                        elif dado2==3:
                            print("jugador {} saca tijera".format(j2))
                        if dado1==1:
                            if dado2==2:
                                print("{} gana 1 punto".format(j2))
                                puntos_j2+=1
                            elif dado2==3:
                                print("{} gana 1 punto".format(j1))
                                puntos_j1+=1
                            else:
                                print("empate")
                        if dado1 == 2:
                            if dado2 == 3:
                                print("{} gana 1 punto".format(j2))
                                puntos_j2 += 1
                            elif dado2 == 1:
                                print("{} gana 1 punto".format(j1))
                                puntos_j1 += 1
                            else:
                                print("empate")
                        if dado1 == 3:
                            if dado2 == 1:
                                print("{} gana 1 punto".format(j2))
                                puntos_j2 += 1
                            elif dado2 == 2:
                                print("{} gana 1 punto".format(j1))
                                puntos_j1 += 1
                            else:
                                print("empate")
                        input("")
                        print("puntos {} = {} \npuntos {} = {}".format(j1,puntos_j1,j2,puntos_j2))
                    j1=""
                    j2=""
