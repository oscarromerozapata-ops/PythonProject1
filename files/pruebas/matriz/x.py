import random
import time
#[elemento, posX,posY,dirX,dirY]
elemento = ["X", 0, 0, 1, 1]
elemento2 = ["0", 1, 0, 1, 1]
dimension = 5
matriz = []
for fila in range(dimension):
    matriz.append([])
    for columna in range(dimension):
        matriz[fila].append(".")

while True:
    time.sleep(2)
    # Matriz Original

    datos = ""
    for fila in range(dimension):
        for columna in range(dimension):
            if fila==elemento[1] and columna==elemento[2]:
                datos = datos+elemento[0].center(5)
            elif fila==elemento2[1] and columna==elemento2[2]:
                datos = datos+elemento2[0].center(5)
            else:
                datos += str(matriz[fila][columna]).center(5)

        datos += "\n"
    if elemento[1] + elemento[3] < 0 or elemento[1] + elemento[3] >= dimension:
        elemento[3] = elemento[3]*(-1)
    elemento[1]=elemento[1]+elemento[3]
    if elemento[2]+elemento[4]<0 or elemento[2]+elemento[4]>=dimension:
        elemento[4]=elemento[4]*(-1)
    elemento[2]=elemento[2]+elemento[4]
    if elemento2[1] + elemento2[3] < 0 or elemento2[1] + elemento2[3] >= dimension:
        elemento2[3] = elemento2[3]*(-1)
    elemento2[1]=elemento2[1]+elemento2[3]
    if elemento2[2]+elemento2[4]<0 or elemento2[2]+elemento2[4]>=dimension:
        elemento2[4]=elemento2[4]*(-1)
    elemento2[2]=elemento2[2]+elemento2[4]
    print(datos)