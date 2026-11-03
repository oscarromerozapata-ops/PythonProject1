menu=("Calculadora\n"+
      "Menu Principal\n"+
      "\n"+
      "1 - Sumar\n"+
      "2 - Restar\n"+
      "3 - Multiplicar\n"+
      "4 - Dividir\n"+
      "0 - Sortir\n")

opcio=1
while opcio !=0:
    print(menu)
    opcio = int(input("Opció:"))
    n1=int(input("Introdueix un numero"))
    n2=int(input("Introdueix un numero"))
    if opcio==1:
        res=n1+n2
        print("Resultat:",res)
    if opcio==2:
        res=n1-n2
        print("Resultat:",res)
    if opcio == 3:
        res = n1*n2
        print("Resultat:", res)
    if opcio == 4:
        if n2==0:
            print("Error")
            continue
        else:
            res = n1 / n2
            print("Resultat:", res)
    input("Presiona una tecla para continuar")
    

