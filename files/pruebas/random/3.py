import random
salir=False
while not salir:
    salir = True
    num=random.randrange(1,4)
    resp= int(input("piedra papel o tijera"))
    if num ==resp:
        print("empate")
        salir = False
    elif num==1 and resp==3:
        print("Guanya la maquina")
    elif num==3 and resp==1:
        print("tu guanyes")
    elif num==3 and resp==2:
        print("Guanya la maquina")
    elif num==2 and resp==3:
        print("tu guanyes")
    elif num==2 and resp==1:
        print("Guanya la maquina")
    elif num==1 and resp==2:
        print("tu guanyes")