precio_total=250000
aportacion_inicial=70000
capital_hipotecado=precio_total-aportacion_inicial
interes_anual=3.5
duracion=15
numero_de_cuotas=duracion*12
interes_mensual=interes_anual/12/100
cuota_mensual=capital_hipotecado*interes_mensual/(1-(1+interes_mensual)**(-numero_de_cuotas))

tabla=("="*75+
      "\nSimulación de hipoteca\n"+
      "="*75+"\n"
      "{:30}{} {}\n".format("Precio total:",precio_total,"€")+
      "{:30}{} {}\n".format("Aportación inicial:",aportacion_inicial,"€")+
      "{:30}{} {}\n".format("Capital hipotecado:",capital_hipotecado,"€")+
      "{:30}{} {}\n".format("Interes anual",interes_anual,"%")+
      "{:30}{} {}\n".format("Duración",duracion,"años")+
      "{:30}{}\n".format("Número de cuotas:",numero_de_cuotas)+
      "{:30}{:0.2f} {}\n".format("Cuota mensual:",cuota_mensual,"€")+
      "\n"+
      "-"*75+"\n"+
      "{:>5}{:>15}{:>15}{:>15}{:>20}\n".format("Mes","Cuota","Intereses","Amortización","Saldo Pendiente")+
      "-"*75+"\n")

mes=0
datos=""
saldo_pendiente=capital_hipotecado
total_intereses=0
total_amortizado=0
for mes in range(1,numero_de_cuotas+1):
      intereses = saldo_pendiente *interes_mensual
      amortizacion = cuota_mensual-intereses
      saldo_pendiente = saldo_pendiente - amortizacion
      total_intereses+=intereses
      total_amortizado+=amortizacion
      datos+="{:5}{:15,.2f}{:15,.2f}{:15,.2f}{:20,.2f}\n".format(mes,cuota_mensual,intereses,amortizacion,saldo_pendiente)

total_pagado_cuotas=numero_de_cuotas*cuota_mensual

final=("-"*75+
       "\n{:25}{:0,.2f}{}\n".format("Total pagado en cuotas: ",total_pagado_cuotas,"€ ")+
       "\n{:25}{:0,.2f}{}\n".format("Total de intereses: ",total_intereses,"€ ")+
       "\n{:25}{:0,.2f}{}\n".format("Total amortizado: ",total_amortizado,"€ ")+
       "\n{:25}{:0,.2f}{}\n".format("Capital inicial: ",capital_hipotecado,"€ "))
print(tabla+datos+final)