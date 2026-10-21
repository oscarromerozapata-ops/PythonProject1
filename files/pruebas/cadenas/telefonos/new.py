cadena = "Pedro*111111111;Anabel*222222222;Jacinta*333333333;Andres*444444444;"
nueva_cadena=""
contacto=""

for i in range(0,cadena.count(";")):
    if i ==0:
        inicio=0
        final=cadena.find(";")
    else:
        inicio=final+1
        final=cadena.find(";",inicio)
    contacto=cadena[inicio:final]
    nombre=contacto[:contacto.find("*")]
    if len(nueva_cadena) == 0:
        nueva_cadena = contacto+";"
    else:
        longitud_cadena2=len(nueva_cadena)
        for j in range (0,nueva_cadena.count(";")):
            if j ==0:
                inicio2=0
                final2=nueva_cadena.find(";")
            else:
                inicio2=final2+1
                final2=nueva_cadena.find(";",inicio2)
            contacto2=nueva_cadena[inicio2:final2]
            nombre2=contacto2[:contacto2.find("*")]
            if nombre<nombre2:
                nueva_cadena=nueva_cadena[:inicio2]+contacto+";"+nueva_cadena[inicio2:]
                break
        if longitud_cadena2==len(nueva_cadena):
            nueva_cadena=nueva_cadena+contacto+";"
cadena = nueva_cadena

print(cadena)
nueva_cadena = ""
contacto = ""
# for i in range(cadena.count(";")):
#     if i == 0:
#         inicio = 0
#         final = cadena.find(";")
#     else:
#         inicio = final + 1  # Ahora el inicio es el final anterior, osea empieza desde el ; del anterior nombre
#         final = cadena.find(";",inicio) # Ahora el final es el ; pero contando desde el inicio de ahora, osea que las ; anterior no los mira
#     contacto = cadena[inicio:final]
#     nombre = contacto[:contacto.find("*")]
#     if len(nueva_cadena) == 0:
#         nueva_cadena = contacto+";"
#     else:
#         longitud_original_nueva_cadena = len(nueva_cadena)
#         # Los nuevo_ o nueva_ son por la nueva_cadena, es el mismo algoritmo
#         # Recorrer nueva cadena e insertar
#         for j in range(nueva_cadena.count(";")):
#             if j == 0:
#                 nuevo_inicio = 0
#                 nuevo_final = nueva_cadena.find(";")
#             else:
#                 nuevo_inicio = nuevo_final + 1
#                 nuevo_final = nueva_cadena.find(";", nuevo_inicio)
#             nuevo_contacto = nueva_cadena[nuevo_inicio:nuevo_final]
#             nuevo_nombre = nuevo_contacto[:nuevo_contacto.find("*")]
#             if nombre < nuevo_nombre:
#                 nueva_cadena = nueva_cadena[:nuevo_inicio] + contacto+";" + nueva_cadena[nuevo_inicio:]
#                 break
#         if len(nueva_cadena) == longitud_original_nueva_cadena:
#             nueva_cadena = nueva_cadena + contacto+";"
# cadena = nueva_cadena
#
# print(cadena)
