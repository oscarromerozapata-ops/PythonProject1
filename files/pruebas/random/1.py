import random

num=random.randrange(1,11)
resp=0
while not num==resp:
    resp=int(input("Dime un número del 1 al 10\n"))
    if not resp==num:
        print("error vuelve a intentarlo")
        input("Enter to continue")
    else:
        print("has encertat enhorabona")