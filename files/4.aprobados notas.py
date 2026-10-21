cabecera=(("Alumnos".center(60,"*")+"\n"+
          "{:20}{:15}{:>10}{:>15}".format("Dni","Nombre","Nota","Nota Boletin"))+"\n"+
          "*"*60)+"\n"
datos=""
dni=input("DNI")
nombre=input("Nombre")
nota=float(input("Nota"))
boletin=""
if nota<5:
    boletin="Suspendido"
elif nota>=5 and nota<6:
    boletin="Aprobado"
elif nota>=6 and nota<7:
    boletin="Bien"
elif nota>=7 and nota<9:
    boletin="Notable"
elif nota>=9:
    boletin="Excelente"

cuerpo="{:20}{:15}{:>10.2f}{:>15}".format(dni,nombre,nota,boletin)+"\n"
datos=datos+cuerpo

dni=input("DNI")
nombre=input("Nombre")
nota=float(input("Nota"))
boletin=""
if nota<5:
    boletin="Suspendido"
elif nota>=5 and nota<6:
    boletin="Aprobado"
elif nota>=6 and nota<7:
    boletin="Bien"
elif nota>=7 and nota<9:
    boletin="Notable"
elif nota>=9:
    boletin="Excelente"

cuerpo="{:20}{:15}{:>10.2f}{:>15}".format(dni,nombre,nota,boletin)+"\n"
datos=datos+cuerpo
print(cabecera+datos)