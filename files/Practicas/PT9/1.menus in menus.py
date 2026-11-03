n="0"
n2="1"
n3="2"
opc=""
menu=("Menu0{}".center(20,"*").format(n)+"\n"
      +"1)Menu0{}".format(n2)+"\n"+
      "2)Menu0{}".format(n3)+"\n"+
      "3)exit")
while not opc=="3":
    print(menu)
    opc = input("Opción: ")
    if opc=="1":
        opc="1"
        input("Has elejido el menú")
    elif opc=="2":
        opc="2"
        input("Has elejido el menú")
    elif opc=="3":
        opc="3"
        input("Saliendo")
        continue
    else:
        input("Opción incorrecta vuelve a intentarlo")
        continue
    n+=opc
    n2=n+"1"
    n3=n+"2"
    menu=("Menu{}".center(20,"*").format(n)+"\n"
          +"1)Menu{}".format(n2)+"\n"+
          "2)Menu{}".format(n3)+"\n"+
          "3)exit")