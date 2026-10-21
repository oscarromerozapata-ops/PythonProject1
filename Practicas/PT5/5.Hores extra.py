hores=int(input("Intrdueix les hores treballades"))
preu=float(input("Introdueix el preu per hora"))

if hores>35:
    extra=(hores-35)*(preu*1.5)
    salario=35*preu+extra
    print("El salario es: ",salario)
else:
    salario=hores*preu
    print("El salario es:",salario)