r1=10
d2=6
e=50
dias=0
while r1>0 and d2 >0 and e>0:
    #Las estaciones de energía E se duplican.
    e=e*2
    dias+=1
    if dias%2==0:
        #Cada robot R1 consume 4 estaciones E para recargarse y se duplica.
        #Si no hay suficientes estaciones, el robot se apaga (muere).
        if 4*r1<=e:
            e_sobreviven=e-4*r1
            r1=r1*2
            e=e_sobreviven
        else:
            e_sobreviven=e%4
            r_cons=e//4
            r1=r_cons*2
            e=e_sobreviven
    if dias%3==0:
        #cada 3 dias
        #cada 2 dornes d2 desactiva 1 robot r1
        r_desactivados=d2//2
        if r1>r_desactivados:
            r1=r1-r_desactivados
        else:
            r1=0
        #Luego, cada dron consume 3 estaciones E para potenciarse y se duplica.
        if 3*d2<e:
            #todos los drones consumen estaciones
            # Si no hay suficientes estaciones, se apaga.
            e_sobreviven= e-3*d2
            d2=2*d2
            e=e_sobreviven
        else:
            e_sobreviven=e%3
            d_consumen_estaciones=e//3
            e=e_sobreviven
            d2=2*d_consumen_estaciones
    if dias%4==0:
        #Cada 50 estaciones sobrecargan y destruyen 2 robots.
        if r1//2> e//50:
            r_destruidos=2*(e//50)
            r1=r1-r_destruidos
        else:
            r1=r1%2
        #Además, cada 4 robots R1 logran hackear y destruyen 1 drone .
        if d2>r1%4:
            d_sobreviven=d2-r1//4
            d2=d_sobreviven
        else:
            d2=0
    print("Dia{}: Robots{}, Drones{}, Estaciones{}".format(dias,r1,d2,e))



