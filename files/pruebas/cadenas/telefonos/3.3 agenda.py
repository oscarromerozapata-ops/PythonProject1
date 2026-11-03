nueva_agenda = ""
                for j in range(0, agenda.count(";")):
                    if j == 0:
                        inicio2 = 0
                        final2 = agenda.find(";")
                    else:
                        inicio2 = final2 + 1
                        final2 = agenda.find(";", inicio2)
                    contacto = agenda[inicio2:final2]
                    primer_separador = contacto.find("*")
                    segundo_separador = contacto.find("*", primer_separador + 1)
                    nombre = contacto[:primer_separador]
                    direccion = contacto[primer_separador + 1:segundo_separador]
                    tfns = contacto[segundo_separador + 1:]
                    for i in range(0, tfns.count("#")):
                        if i == 0:
                            inicio = 0
                            final = tfns.find("#")
                            datos = datos + str(j + 1) + ")" + "{:20}{:20}{:>20}\n".format(nombre, direccion,
                                                                                           tfns[inicio:final])
                        else:
                            inicio = final + 1
                            final = tfns.find("#", inicio)
                            datos = datos + "{:20}{:20}{:>20}\n".format("", "", tfns[inicio:final])
                    datos = datos + "-" * 60 + "\n"
                datos = datos + str(j + 2) + ")Salir\n"
                print(datos)
                datos = ""
                opc = input("Cual contacto desea eliminar el telefono?")
                nuevo_tel = input("escribe el numero que desea borrar")
                if not opc.isdigit():
                    print("Error introduce una opción numerica")
                elif not int(opc) in range(1, agenda.count(";") + 2):
                    print("opción fuera de rango")
                    input("Enter to continue")
                else:
                    opc = int(opc)
                    if opc == agenda.count(";") + 1:
                        flg_menu03 = False
                        flg_menu00 = True
                    else:
                        for j in range(0, agenda.count(";")):
                            if j == 0:
                                inicio2 = 0
                                final2 = agenda.find(";")
                            else:
                                inicio2 = final2 + 1
                                final2 = agenda.find(";", inicio2)
                            contacto = agenda[inicio2:final2]
                            primer_separador = contacto.find("*")
                            segundo_separador = contacto.find("*", primer_separador + 1)
                            nombre = contacto[:primer_separador]
                            direccion = contacto[primer_separador + 1:segundo_separador]
                            tfns = contacto[segundo_separador + 1:]
                            if j + 1 == opc:
                                inicio4=contacto.find(nuevo_tel)
                                for i in range(0, tfns.count("#")):
                                    if i == 0:
                                        inicio = 0
                                        final = tfns.find("#")
                                    else:
                                        inicio = final + 1
                                        final = tfns.find("#", inicio)
                                    if nuevo_tel in tfns[inicio:final]:
                                        tfns = tfns[:inicio] + tfns[final+1:]
                            contacto=nombre+"*"+direccion+"*"+tfns
                            nueva_agenda = nueva_agenda + contacto + ";"
                            for i in range(0, tfns.count("#")):
                                if i == 0:
                                    inicio = 0
                                    final = tfns.find("#")
                                    datos = datos + str(j + 1) + ")" + "{:20}{:20}{:>20}\n".format(nombre, direccion,
                                                                                                   tfns[inicio:final])
                                else:
                                    inicio = final + 1
                                    final = tfns.find("#", inicio)
                                    datos = datos + "{:20}{:20}{:>20}\n".format("", "", tfns[inicio:final])
                            datos = datos + "-" * 60 + "\n"
                    print(datos)
                    agenda = nueva_agenda
                    print(agenda)
                    datos = ""
                    input()