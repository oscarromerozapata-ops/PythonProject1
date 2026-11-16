letrasDni = ('T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E')
usuario1 = {"nombre":"Pedro Javier Morales",  "direccion": "Flores 36 8º 2º", "tfn":["+0034345345345"],"compras":[1234,423,23]}
usuario2 = {"nombre":"Maite Lopez Miravet", "direccion":"Balmes 31 1º 2º","tfn":["+0034234234235","+0034239999235"],"compras":[12344]}
usuario3 = {"nombre":"Marta Garcia Suarez",  "direccion":"Valencia 21 3º 1º","tfn": ["+0075766576575"],"compras":[34,423,23,6]}
usuarios = {"47474747X":usuario1,"24536425T":usuario2,"76767676H":usuario3}

cabecera="{:12}{:25}{:20}{:20}{:15}\n".format("DNI","nombre","direccion","tfn","Total Compras")
datos=""

for dni in usuarios:
    suma_compras=0
    for compra in usuarios[dni]["compras"]:
        suma_compras+=compra
    datos=datos+"{:12}{:25}{:20}{:20}{:15}\n".format(dni,usuarios[dni]["nombre"],usuarios[dni]["direccion"],usuarios[dni]["tfn"][0],str(suma_compras))

    str(suma_compras)
    if len(usuarios[dni]["tfn"])>1:
        for i in range(1,len(usuarios[dni]["tfn"])):
            datos = datos + "{:12}{:25}{:20}{:20}{:25}{:15}\n".format("","","",usuarios[dni]["tfn"][i],"","")
    datos=datos + "*"*90+"\n"
print(cabecera+datos)