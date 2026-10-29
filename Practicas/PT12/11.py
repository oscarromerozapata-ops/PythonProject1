cadena="ASDfdsfFDSFDSfds  F  "
contador=0
conte="No conte digit"
for i in cadena:
    if i.isdigit():
        conte="Si conte digit"
        break
print(conte)