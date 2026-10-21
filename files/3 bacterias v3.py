b1=100
b2=50
ca=100

seg=1
while (b1>0 and ca>0) or (b2>0 and ca>0)or(b1>0 and b2>0):
    #cada 1 segundo:las celulas CA, se duplican
    ca=ca*2

    if seg%2==0:
        # Cada 2 segundos:
        #   * cada bacteria B1 se come 3 celulas CA y se dublica, en caso de no
        #   tener suficientes celulas para comer, se muere.
        if b1*3<=ca:
            ca=ca-b1*3
            b1=b1*2
        else:
            b1_restantes=ca//3
            ca_muertas=ca%3
            b1=b1_restantes*2
            ca=ca_muertas
    if seg%3==0:
# cada 3 segundos:
#   * cada 2 bacterias B2 matan 1 bacteria B1
#   * cada bacteria B1 se come 2 celulas CA y se duplica, en caso de no tener suficientes celulas para comer, se muere.
        if b1>b2//2:
            b1=b1 - b2 // 2
        else:
            b1=0
        if b2*2<ca:
            ca_muertas=ca-b2*2
            b2=b2*2
            ca=ca_muertas
        else:
            b2_restanes=ca//2
            ca_restantes=ca%2
            b2=b2_restanes*2
            ca=ca_restantes

    if seg%4==0:
# cada 4 segundos:
#   * cada 5 celulas CA, matan una Bacteria B1
#   * cada 3 Bacterias B1 matan una B2
        if b1>=ca//5:
            b1=b1-ca//5
        else:
            b1=0
        if b2>=b1//3:
            b2=b2-b1//3
        else:
            b2=0

    print ("segundos{}: b1 {}, b2 {}, ca {}".format(seg,b1,b2,ca))
    seg += 1