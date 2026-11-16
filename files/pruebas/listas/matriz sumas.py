import random
matriz=[]
dimension=4
for fila in range(dimension):
    matriz.append([])
    for columna in range(dimension):
        matriz[fila].append(random.randint(0,10))
print(matriz)

datos=""
for fila in range(dimension):
    for columna in range(dimension):
        datos=datos+str(matriz[fila][columna]).rjust(5)
    datos=datos+"\n"
print(datos)
#izquierda a derecha
"""for fila in range(dimension):
    for pasada in range(dimension - 1):
        ordenado = True
        for i in range(dimension - 1):
            if matriz[fila][i] > matriz[fila][i + 1]:
                ordenado = False
                aux = matriz[fila][i]
                matriz[fila][i] = matriz[fila][i + 1]
                matriz[fila][i + 1] = aux
        if ordenado:
            break

datos=""
for fila in range(dimension):
    for columna in range(dimension):
        datos=datos+str(matriz[fila][columna]).rjust(5)
    datos=datos+"\n"
print(datos)

for columna in range(dimension):
    for pasada in range(dimension - 1):
        for i in range(dimension - 1 - pasada):
            if matriz[i][columna] > matriz[i+1][columna]:
                aux=matriz[i][columna]
                matriz[i][columna] = matriz[i+1][columna]
                matriz[i+1][columna] = aux
datos=""
for fila in range(dimension):
    for columna in range(dimension):
        datos=datos+str(matriz[fila][columna]).rjust(5)
    datos=datos+"\n"
print(datos)
"""
#derecha a izquierda

for fila in range(dimension):
    for pasada in range(dimension - 1):
        ordenado = True
        for i in range(dimension - 1,pasada,-1):
            if matriz[fila][i] < matriz[fila][i - 1]:
                ordenado = False
                aux = matriz[fila][i]
                matriz[fila][i] = matriz[fila][i - 1]
                matriz[fila][i -1] = aux
        if ordenado:
            break

datos=""
for fila in range(dimension):
    for columna in range(dimension):
        datos=datos+str(matriz[fila][columna]).rjust(5)
    datos=datos+"\n"
print(datos)

for columna in range(dimension):
    for pasada in range(dimension - 1):
        for i in range(dimension-1, pasada,-1):
            if matriz[i][columna] < matriz[i-1][columna]:
                aux=matriz[i][columna]
                matriz[i][columna] = matriz[i-1][columna]
                matriz[i-1][columna] = aux
datos=""
for fila in range(dimension):
    for columna in range(dimension):
        datos=datos+str(matriz[fila][columna]).rjust(5)
    datos=datos+"\n"
print(datos)