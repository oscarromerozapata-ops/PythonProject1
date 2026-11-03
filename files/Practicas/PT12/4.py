#Una dupla s’escriu (a, b) i correspon a un par d’elements, per exemple, (1, ‘a’) és
#una dupla. Escriu una seqüencia que generi totes les duples dels números del 0 al 9 amb les
#lletres de l’alfabet.


llista=[]
for i in range(0,10):
    num = 64
    letra = ""
    while not letra=="Z":
        num=num+1
        letra=chr(num)
        print(letra)
        new=letra,i
        llista.append(new)
print(llista)

