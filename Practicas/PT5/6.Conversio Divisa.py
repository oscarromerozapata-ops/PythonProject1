tabla=("="*31+"\n"+
       "= 1.- Euros a Dolar"+"\n"+
       "= 2.- Euros a Yens"+"\n"+
       "= 3.- Dolar a Euro"+"\n"+
       "= 4.- Dolar a Yens"+"\n"+
       "= 5.- Yens a Euro"+"\n"+
       "= 6.- Yens a Dolar"+"\n"+
       "="*31+"\n"+
       "= Tria una Opció de conversió ="+"\n"+
       "="*31)
print (tabla)
opcio=int(input("a"))
yen=115.998
dolar=1.11894
euro=1
resultado=0
cantidad=float(input("Escribe la cantidad de conversión"))
if opcio==1:
       resultado+=cantidad*dolar
elif opcio==2:
       resultado+=cantidad*yen
elif opcio==3:
       resultado+=cantidad/dolar
elif opcio==4:
       resultado+=(cantidad/dolar)*yen
elif opcio==5:
       resultado+=cantidad/yen
elif opcio==6:
       resultado+=(cantidad/yen)*dolar
print (resultado)