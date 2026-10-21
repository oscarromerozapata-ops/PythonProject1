#tiene qeu ser 12 dias
cazadores=6
lobos=8
ovejas=12
dia=1
while cazadores >0 and lobos>0 and ovejas>0:
    #Cada 5 ovejas generan una nueva oveja
    ovejas=ovejas+ovejas//5
    if dia%2==0:
        #cada 2 dias
        #Cada 3 lobos  se comen  1 oveja y estos 3 lobos crean un nuevo lobo. Si algun lobo no encuentra más
        # un grupo de 2 lobos más para cazar, muere.
        # Si no hay suficientes ovejas los lobos que no cazan mueren.
        # Viene un nuevo cazador al pueblo
        if ovejas>=lobos//3:
            lobos_comen=lobos//3
            ovejas=ovejas-lobos_comen
            lobos=lobos_comen+lobos_comen*3
        else:
            lobos_comen=ovejas//3
            lobos=lobos_comen+lobos_comen*3
            ovejas=0
        cazadores=cazadores+1
    if dia%3==0:
        #Cada 3 dias:
        # Cada 2 cazadores matan un lobo.
        # Luego, cada 2 lobos sobrevivientes se come 1 oveja y de estos lobos nace un nuevo lobo. Si un
        # lobo no encuentra otro lobo que le acompañe cazando ovejas, muere.
        # Lo lobos que no tengan ovejas para cazar mueren .
        lobos=lobos-cazadores//2
        if lobos<0:
            lobos=0
        if ovejas>lobos//2:
            lobos_comen=lobos//2
            ovejas=ovejas-lobos_comen
            lobos=lobos_comen+lobos_comen*2
    if dia%4==0:
        #Cada 4 dias:
        # Cada 30 ovejas matan un lobo.
        #Además, cada 10 lobos matan un cazador.
        lobos=lobos-ovejas//30
        if lobos<0:
            lobos=0
        cazadores=cazadores-lobos//10
        if cazadores<0:
            cazadores=0
    print("dia={} lobos={} ovejas={} cazadores={}".format(dia,lobos,ovejas,cazadores))
    dia = dia + 1

