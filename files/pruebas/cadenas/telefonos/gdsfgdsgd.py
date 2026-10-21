agenda="Pedro*Balmes 27*111111111#333425325#+4534553453#;Jacinta*Ardur 32*333333333#657483746#;Andres*Arriba 1**444444444#374658365#;Anabel*Derecha 3**222222222#465768347#;"
datos=""
opciones=""
for i in range (0,agenda.count(";")):
    if i == 0:
        inicio=0
        final=agenda.find(";")
    else:
        inicio=final+1
        final=agenda.find(";",inicio)
    contacto=agenda[inicio:final]
    primer_separador=contacto.find("*")
    segundo_separador=contacto.find("*",primer_separador+1)

    nombre=contacto[:primer_separador]
    direccion=contacto[primer_separador+1:segundo_separador]
    tfns=contacto[segundo_separador+1:]
    opciones = opciones + str(i + 1) + ")" + "{:20}{:20}\n".format(nombre, direccion)
opciones = opciones + str(i + 2) + ")" + "Salir"
print(opciones)