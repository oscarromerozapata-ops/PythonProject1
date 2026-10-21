ampla=input("Ampla del rectangle: ")
while not ampla.isdigit():
    ampla = input("Error, introdueix l'ampla del rectangle: ")
alcada=input("Alçada del rectangle: ")
while not alcada.isdigit():
    alcada = input("Error, introdueix l'alçada del rectangle: ")
alcada=alcada-2
espais=" "*(ampla-2)
print("*"*ampla)
while alcada!=0:
    print("*"+espais+"*")
    alcada=alcada-1
print("*"*ampla)