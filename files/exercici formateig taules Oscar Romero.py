cabecera=(" Magatzem Logistic ".center(60,"*")+"\n"+
          "{:30}{:>10}{:>10}{:>10}\n".format("Producte","Quantitat","Preu","Total")
          +"*"*60+"\n")
datos=""

Producte=input("Producte")
Quantitat=int(input("Quantitat"))
Preu=float(input("Preu"))
Total=Quantitat*Preu
todo=Quantitat*Preu
tabla="{:30}{:>10}{:>10.3f}{:>10.2f}\n".format(Producte, Quantitat, Preu, Total)
datos=datos+tabla

Producte=input("Producte")
Quantitat=int(input("Quantitat"))
Preu=float(input("Preu"))
Total=Quantitat*Preu
todo+=Quantitat*Preu
tabla="{:30}{:>10}{:>10.3f}{:>10.2f}\n".format(Producte, Quantitat, Preu, Total)
datos=datos+tabla

Producte=input("Producte")
Quantitat=int(input("Quantitat"))
Preu=float(input("Preu"))
Total=Quantitat*Preu
todo+=Quantitat*Preu
tabla="{:30}{:>10}{:>10.3f}{:>10.2f}\n".format(Producte, Quantitat, Preu, Total)
datos=datos+tabla
pie="*"*60+"\n{:>60}\n{:60.2f}".format("Precio Total:",todo)

print(cabecera+datos+pie)