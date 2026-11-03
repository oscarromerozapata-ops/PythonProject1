hora=30
metre=0.5
iva=0.21
print(type(metre))
horest=int(input("Introdueix les hores treballades"))
metresi=int(input("Introdueix els metres instalats"))

preu=horest*hora
preuiva=preu-(preu*iva)

print("El preu brut es: ",preu)
print("El preu amb el iva es: ",preuiva)