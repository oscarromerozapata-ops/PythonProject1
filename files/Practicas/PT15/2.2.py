dada1=[2005,11,19]
dada2=[2026,11,12]

dias=0
dias=dias+365*(dada1[0]%dada2[0])
dias=dias+30*(dada1[1]%dada2[1])
dias=dias+dada1[2]%dada2[2]

print(dias)