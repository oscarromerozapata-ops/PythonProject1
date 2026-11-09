import random
dimension=4
matriz=[]
for fila in range(dimension):
    matriz.append([])
    for columna in range(dimension):
        matriz[fila].append(random.randint(1,100))
datos=""
for fila in range(dimension):
    for columna in range(dimension):
        datos=datos+str(matriz[fila][columna]).rjust(5)
    datos=datos+"\n"
print(datos)

datos=""
for fila in range(dimension-1,-1,-1):
    for columna in range(dimension):
        datos=datos+str(matriz[fila][columna]).rjust(5)
    datos=datos+"\n"
print(datos)