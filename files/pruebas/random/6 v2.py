import random
ranking=""
jugador_usuario = ""
puntos_a=0
puntos_d=0
limite_puntos=30
victorias_a=0
victorias_d=0
jugador_maquina="BOT"
puntos_maquina=0
puntos_usuario=0
victorias_usuario=0
victorias_maquina=0
menu_principal="1)Usuario\n2)Jugar\n3)Ranking\n4)Salir"
salir= False
while not salir:
    print(menu_principal)
    opc = input("Opción: ")
    if not opc.isdigit():
        print("Opción no mumerica")
        input("Enter")
    elif int(opc)>0 and int(opc)>4:
        print("Opción fuera de rango")
    else:
        opc=int(opc)
        if opc==1:
            jugador_usuario=input("Introduce nombre de usuario")
        if opc==2:
            if jugador_usuario == "":
                print("usuario en blanco")
                input("Enter")
            else:
                while puntos_maquina<limite_puntos and puntos_usuario<limite_puntos:
                    num=random.randint(1,2)
                    da1 = 0
                    da2 = 0
                    da3 = 0
                    da4 = 0
                    da5 = 0
                    dd1 = 0
                    dd2 = 0
                    dd3 = 0
                    puntos_a = 0
                    puntos_d = 0
                    for i in range(5):
                        da=random.randint(1,6)
                        if da>da1:
                            da5=da4
                            da4=da3
                            da3=da2
                            da2=da1
                            da1=da
                        elif da>da2:
                            da5 = da4
                            da4 = da3
                            da3 = da2
                            da2 = da
                        elif da>da3:
                            da5 = da4
                            da4 = da3
                            da3 = da
                        elif da>da4:
                            da5 = da4
                            da4 = da
                        elif da>da5:
                            da5 = da
                    for j in range(3):
                        dd = random.randint(1, 6)
                        if dd>dd1:
                            dd3=dd2
                            dd2=dd1
                            dd1=dd
                        elif dd>dd2:
                            dd3=dd2
                            dd2=dd
                        elif dd>dd3:
                            dd3=dd
                    if dd1>=da1 :
                        puntos_d+=1
                    else:
                        puntos_a += 1
                    if dd2>=da2:
                        puntos_d += 1
                    else:
                        puntos_a += 1
                    if dd3>=da3:
                        puntos_d += 1
                    else:
                        puntos_a += 1
                    if puntos_a>puntos_d:
                        if num == 1:
                            victorias_maquina+= 1
                        elif num == 2:
                            victorias_usuario += 1
                    else:
                        if num == 2:
                            victorias_maquina += 1
                        elif num == 1:
                            victorias_usuario += 1
                    if num==1:
                        puntos_maquina+=puntos_a
                        puntos_usuario+=puntos_d
                    elif num==2:
                        puntos_maquina+= puntos_d
                        puntos_usuario+= puntos_a
                    menu= ("DADOS".center(35,"=")+"\n"+
                            "{:15}{:3}{:3}{:3}{:3}{:3}\n".format("Dados Atacante:",da1,da2,da3,da4,da5)+
                            "{:15}{:3}{:3}{:3}{:3}{:3}\n".format("Dados Defensor:",dd1,dd2,dd3,"","")+
                            "PUNTOS".center(35,"=")+"\n"+
                            "Puntos Atacante: {}\n".format(puntos_a)+
                            "Puntos Defensor: {}\n".format(puntos_d)+
                            "="*35+"\n"+
                            "Puntos {}: {}\n".format(jugador_maquina,puntos_maquina)+
                            "Puntos {}: {}\n".format(jugador_usuario,puntos_usuario)+
                            "Victorias {}: {}\n".format(jugador_maquina, victorias_maquina) +
                            "Victorias {}: {}\n".format(jugador_usuario, victorias_usuario)
                            )
                    print (menu)
                if puntos_usuario>=limite_puntos:
                    ranking += "{}: {}\n".format(jugador_usuario, puntos_usuario)
                puntos_maquina = 0
                puntos_usuario = 0
                jugador_usuario = ""
        if opc==3:
            print(ranking)
        if opc==4:
            salir=True