agenda = [
    ["Alberto Castaño Sanchez", "Balmes 27 1º2º ", ["666344551","777000000"]],
    ["Enrique Casado Ruiz" , "Rocafort 234 5º1º" ,["674343536","937182323","345343434"]],
    ["Esther Flores Ruiz", "Numancia 345 10º A", ["657876543"]],
    ["Maria Lopez Vallejo", "Bonavista 43 3º3º" , ["667344556","937249898"]]
]
cabecera="Agenda".center(70,"=")+"\n"+"{:30}{:20}{:>20}\n".format("Nombre","Direccion","Numero")+"="*70+"\n"
datos=""
menu00="1)View contacts\n2)New contact\n3)Edit contact\n4)Remove contact\n5)Search contact\n6)salir"
menu03="1)Edit direction\n2)Add tfn\n3)Remove tfn\n4)back"
menu05="1)Search by name\n2)Search from direction\n3)Search by num\n4)back"
salir=False
flg_menu00=True
flg_menu03=False
flg_menu04=False
datos=""
for i in range (0,len(agenda)):
    nom=agenda[i][0]
    direccion=agenda[i][1]
    num=str(agenda[i][2])
    for j in range (len(agenda[i][2])):
        if j==0:
            datos = datos + "{:30}{:20}{:>20}\n".format(nom, direccion, agenda[i][2][j])
        else:
            datos = datos + "{:30}{:20}{:>20}\n".format("", "", agenda[i][2][j])
    datos=datos+"-"*70+"\n"
print(cabecera+datos)
