#La funció chr(a) retorna el caràcter amb codi ASCII a, per
#exemple, chr(65) == ‘A’. Escriu una seqüencia que generi les lletres de la A a la Z.
num=64
letra=""
while not letra=="Z":
    num=num+1
    letra=chr(num)
    print(letra)
