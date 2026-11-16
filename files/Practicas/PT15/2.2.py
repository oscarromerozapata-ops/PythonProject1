dada1=[2005,11,19]
dada2=[2026,11,16]


if dada1[0]>dada2[0]:
    anos=dada1[0]%dada2[0]*365
else:
    anos=dada2[0]%dada1[0]*365

if dada1[1]>dada2[1]:
    meses=(dada1[1]%dada2[1])*30
else:
    meses=(dada2[1]%dada1[1])*30

if dada1[2]>dada2[2]:
    dias=(dada1[2]%dada2[2])+anos+meses
else:
    dias = (dada2[2] % dada1[2]) + anos+meses

print(dias)