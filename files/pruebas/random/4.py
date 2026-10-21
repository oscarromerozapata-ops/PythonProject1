import random
A=0
B=0
salir=False

while not salir:
    A = random.randrange(10)
    B = random.randrange(10)
    print(A, B)
    while A == B:
        A = random.randrange(10)
        B = random.randrange(10)
        print(A,B)
    num=input("Apostes per A o B")
    while not (num=="A" or num=="B"):
        num = input("Apostes per A o B")
    if A>B:
        if num=="A":
            print("Has guanyat")
        else:
            print("Has perdut")
    else:
        if num == "B":
            print("Has guanyat")
        else:
            print("Has perdut")
    parar=False
    while not parar:
        res=input("Vols provar un altre cop?")
        if res=="N":
            salir=True
            parar=True
        elif res=="S":
            parar=True
            input("Continuem")
        else:
            print("torna a intentar")