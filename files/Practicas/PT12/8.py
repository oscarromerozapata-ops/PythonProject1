numeros=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
dni=int(input("Ingrese el dni: "))
dni=dni%23
letra=numeros[dni]
print(letra)