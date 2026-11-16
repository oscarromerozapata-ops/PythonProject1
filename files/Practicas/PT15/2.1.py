dias_mes = [31, 28, 31, 30,31, 30, 31, 31,30, 31, 30, 31]

anno=input("año")
dia=int(input("dia"))
mes=int(input("mes"))

for i in range (len(dias_mes)):
    if dia+1>dias_mes[mes]:
        dia=1
        mes=mes+1
        print(anno,mes+1,dia)
    else:
        dia=dia+1
        print(anno, mes + 1, dia)

