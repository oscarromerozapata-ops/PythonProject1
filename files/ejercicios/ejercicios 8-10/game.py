import random
menu00="The Best Game In The World".center(40,"=")+"\n1)New Game\n2)New Player\n3)Show Ranking\n4)Exit"
jugador_bot="BOT"
jugador_usuario=""
ranking="Ranking".center(20,"=")+"\n{:10}{:>10}\n".format("Name","Points")
salir=False

limite_puntos=50
while not salir:
    print(menu00)
    opc = input("option:")
    if not opc.isdigit():
        print("Error, opción no numerica")
        input("Enter to continue")
    elif int(opc)<1 or int(opc)>4:
        print("Error, opción fuera de rango")
        input("Enter to continue")
    else:
        opc=int(opc)
        if opc==1:
            if jugador_usuario=="":
                print("Error introduce un nombre de usuario")
            else:
                puntos_jugador=0
                puntos_bot=0
                while puntos_bot<limite_puntos and puntos_jugador<limite_puntos:
                    partida=""
                    ronda=""
                    puntos_ronda_jugador = 0
                    puntos_ronda_bot = 0
                    for i in range(1,3):
                        tirar = True
                        while tirar:
                            d1 = random.randint(1,6)
                            d2 = random.randint(1, 6)
                            d3 = random.randint(1, 6)
                            d4 = random.randint(1, 6)
                            if d1==d2 or d1==d3 or d1==d4 or d2==d3 or d2==d4 or d3==d4:
                                if d1==d2 and d2==d3 and d3==d4:
                                    if i==1:
                                        puntos_jugador+=15
                                        puntos_ronda_jugador += 15
                                        tirar = True
                                    elif i==2:
                                        puntos_bot+=15
                                        puntos_ronda_bot += 15
                                        tirar = True
                                elif (d1==d2 and d2==d3) or (d1==d2 and d2==d4) or (d1==d3 and d3==d4) or (d2==d3 and d3==d4):
                                    if i==1:
                                        puntos_jugador+=8
                                        puntos_ronda_jugador += 8
                                        tirar = True
                                    elif i==2:
                                        puntos_bot+=8
                                        puntos_ronda_bot += 8
                                        tirar = True
                                else:
                                    if i==1:
                                        puntos_jugador+=2
                                        puntos_ronda_jugador += 2
                                        tirar = False
                                    elif i==2:
                                        puntos_bot+=2
                                        puntos_ronda_bot += 2
                                        tirar = False
                            else:
                                tirar = False
                            if i ==1:
                                partida +="Dados de {:20}{:5}{:5}{:5}{:5}\n".format(jugador_usuario,d1,d2,d3,d4)
                            elif i==2:
                                partida += "Dados de {:20}{:5}{:5}{:5}{:5}\n".format(jugador_bot, d1, d2, d3, d4)
                    ronda=("Puntos de {} Ronda={} Total={}\n".format(jugador_usuario,puntos_ronda_jugador,puntos_jugador)+
                            "Puntos de {} Ronda={} Total={}\n".format(jugador_bot,puntos_ronda_bot,puntos_bot))
                    print(partida+ronda)
                    input("Enter to continue")
                if puntos_jugador>=limite_puntos:
                    ranking+="{:10}{:10}\n".format(jugador_usuario,puntos_jugador)
        if opc == 2:
            jugador_usuario=input("Ingrese el nombre del jugador")
        if opc == 3:
            print(ranking)
            input("Enter to continue")