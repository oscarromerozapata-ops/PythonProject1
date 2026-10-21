insertar="Esteban*555555555"
cadena = "Pedro*111111111#333333333;Anabel*222222222;Jacinta*333333333;Andres*444444444;"
cadena2=""
longitud_inicial2= len(cadena)
nombre = ""
nombre2 = ""

# for i in range(0,cadena.count(";")):
#     if i ==0:
#         inicio=0
#         final=cadena.find(";")
#     else:
#         inicio=final+1
#         final=cadena.find(";",inicio)
#     nombre=cadena[inicio:final]
#     if len(cadena2)==0:
#         if insertar<nombre and not insertar=="":
#             cadena2=insertar+";"+nombre+";"
#             insertar=""
#         else:
#             cadena2=nombre+";"
#     else:
#         longitud_inicial=len(cadena2)
#         for j in range(0,cadena2.count(";")):
#             if j==0:
#                 inicio2=0
#                 final2=cadena2.find(";")
#             else:
#                 inicio2=final2+1
#                 final2=cadena2.find(";",inicio2)
#             nombre2=cadena2[inicio2:final2]
#             if insertar<nombre2 and not insertar=="":
#                 cadena2 = cadena2[:inicio2] + insertar + ";" + cadena2[inicio2:]
#                 insertar=""
#             if nombre<nombre2:
#                 cadena2=cadena2[:inicio2]+nombre+";"+cadena2[inicio2:]
#                 break
#         if len(cadena2)==longitud_inicial:
#             cadena2=cadena2+nombre+";"
# #     if nombre_incluir<nombre:
# #         cadena=cadena[:inicio]+nombre_incluir+";"+cadena[inicio:]
# #         break
# if len(cadena2)==longitud_inicial2:
#     cadena2=cadena2+insertar+";"
#
# print(cadena2)

