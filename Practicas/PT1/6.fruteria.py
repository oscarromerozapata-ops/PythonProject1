menu=("NUM. DE KILOS COMPRATS".ljust(30)+"%Descompte".rjust(15)+"\n"+
      "0-2".ljust(30)+"0%".center(15)+"\n"+
      "2.01-5".ljust(30)+"10%".center(15)+"\n"+
      "5.01-10".ljust(30)+"15%".center(15)+"\n"+
      "10.01 en endevant".ljust(30)+"20%".center(15)+"\n")

print (menu)
p=int(input("Quantes pomes vas a comprar"))
preu=float(input("Preu de cada poma"))
if 0<p:
    if p<=2:
        print("No té descompte, preu: ",p*preu,"€")
    elif p<=5:
        print("Descompte de 10%, preu: ",p*(preu-(preu*0.10)),"€")
    elif p<=10:
        print("Descompte de 15%, preu: ",p*(preu-(preu*0.15)),"€")
    elif p>10.01:
        print("Descompte de 20%, preu: ",p*(preu-(preu*0.20)),"€")