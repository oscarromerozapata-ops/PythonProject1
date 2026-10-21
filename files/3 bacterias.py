b1=100
b2=50
ca=100
salida=True
seg=0
while salida:
    ca=ca*2
    seg+=1
    if seg%2==0:
        if ca>b1*3:
            ca=(ca-(b1*3))
            ca=ca*2
        elif ca<b1*3:
            print("La celula se ha muerto")
            input()
            break
    if seg%3==0:
        b1=b1-(b2/2)
        if ca>0:
            ca=ca-(b1*2)
            b1=b1*2
        elif ca<=0:
            print("La celula se ha muerto")
            input()
            break
    if seg%4==0:
        b1=b1-(ca/5)
        b2=b2-(b1/3)
print ("segundos{}: b1{}, b2{}, ca{}".format(seg,b1,b2,ca))