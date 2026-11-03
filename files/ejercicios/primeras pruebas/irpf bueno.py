primer=12450*0.19
segundo=(20199-12450)*0.24
tercer=(35200-20200)*0.30
cuarto=(60000-35200)*0.37
quinto=(300000-60000)*0.45
sueldo_bruto=222222
pago=0
if sueldo_bruto<12450:
    pago+=sueldo_bruto*0.19
elif sueldo_bruto<20200:
    pago+=primer+(sueldo_bruto-12450)*0.24
elif sueldo_bruto<35200:
    pago+=primer+segundo+(sueldo_bruto-20200)*0.30
elif sueldo_bruto<60000:
    pago+=primer+segundo+tercer+(sueldo_bruto-35200)*0.37
elif sueldo_bruto<300000:
    pago += primer + segundo + tercer+cuarto+(sueldo_bruto - 60000) * 0.45
else:
    pago += primer + segundo + tercer+cuarto+quinto +(sueldo_bruto - 300000) * 0.47

print(pago)