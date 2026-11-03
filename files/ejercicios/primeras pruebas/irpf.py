cobro=int(input("Escribe la cantidad que has generado"))

if cobro<12450:
    pago=cobro*0.19
elif cobro>12450:
    pago = cobro * 0.19
    cuenta=cobro-12450
    if cuenta<7749:
        pago+=cuenta*0.24
    elif cuenta>7749:
        pago += cuenta * 0.24
        cuenta=cuenta-15000
        if cuenta < 15000:
            pago += cuenta * 0.30
        elif cuenta > 24800:
            pago += cuenta * 0.30
            cuenta = cuenta - 24800
            if cuenta < 25800:
                pago += cuenta * 0.37
            elif cuenta > 25800:
                pago += cuenta * 0.37
                cuenta = cuenta - 7749
                if cuenta < 240000:
                    pago += cuenta * 0.45
                elif cuenta > 240000:
                    pago += cuenta * 0.45
                    cuenta = cuenta - 7749
                    if cuenta > 1:
                        pago += cuenta * 0.47
print("Tienes que pagar :",pago)
