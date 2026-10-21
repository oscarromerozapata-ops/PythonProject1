cabecera= ("*" * 30+"\n"+str("comida").center(30)+"\n"+"*" * 30+
           "\n"+str("Nombre").ljust(15)+str("precio").rjust(14))
cuerpo =("\n"+str("Entrecot").ljust(15)+str("23,35").rjust(14)+"\n"+
        str("Callos").ljust(15)+str("15,1").rjust(14)+"\n"+
        str("Patatass Bravas").ljust(15)+str("9,5").rjust(14))

print(cabecera+cuerpo)