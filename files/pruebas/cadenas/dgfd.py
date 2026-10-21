cadena= "Pedro;Paco;Anabel;Lucia;Andres;"
c=""
for i in range (len(cadena)):
    if cadena[i].isalpha():
        c=c+cadena[i]
    else:
        print(c)
        c=""