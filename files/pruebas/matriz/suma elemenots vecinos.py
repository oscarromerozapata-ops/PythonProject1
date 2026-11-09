dimension = 3

num = 0
matriz = []
for fila in range(dimension):
    matriz.append([])
    for columna in range(dimension):
        num += 1
        matriz[fila].append(num)

new_matriz = []
for new_fila in range(dimension):
    new_matriz.append([])
    for new_columna in range(dimension):
        new_matriz[new_fila].append(0)
        for fila in range(new_fila-1,new_fila+2):
            for columna in range(new_columna-1,new_columna+2):
                if (fila>=0 and fila<dimension and columna>=0 and columna<dimension and (fila!=new_fila or columna!=new_columna)):
                    new_matriz[new_fila][new_columna] =new_matriz[new_fila][new_columna]+ matriz[fila][columna]



# Matriz Original
datos = ""
for fila in range(dimension):
    for columna in range(dimension):
        datos += str(matriz[fila][columna]).rjust(5)
    datos += "\n"
print(datos)

# Suma de los números de la misma fila, sin contarse a si mismo
datos = ""
for fila in range(dimension):
    for columna in range(dimension):
        datos += str(new_matriz[fila][columna]).rjust(5)
    datos += "\n"
print(datos)

# Original:
#     1    2    3
#     4    5    6
#     7    8    9

# Suma de los números de la misma fila, sin contarse a si mismo:
#     5    4    3
#    11   10    9
#    17   16   15
#
