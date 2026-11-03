ampla=input("Ampla del rectangle: ")
alcada=input("Alçada del rectangle: ")
alcada=alcada-2
espais=" "*(ampla-2)
print("*"*ampla)
while alcada!=0:
    print("*"+espais+"*")
    alcada=alcada-1
print("*"*ampla)