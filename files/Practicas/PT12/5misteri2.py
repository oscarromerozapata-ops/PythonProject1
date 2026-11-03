from math import ceil
grados=float(input("Ingrese la cantidad de grados"))

cuadrante=int(ceil(grados) %360)/90

if cuadrante==0:
    #angulo de 0 grados
    print("primer cuadrante")
if cuadrante==1:
    #angulo de 90 grados
    print("segundo cuadrante")
if cuadrante==2:
    #angulo de 180 grados
    print("terceiro cuadrante")
if cuadrante==3:
    #angulo de 270 grados
    print("quartos cuadrantes")