num=input("introduce un numero")
num=int(num)
desc=""
no=num
co=0
for i in range(2,num//2):
    cont=0
    primo=True
    for j in range(2,i//2):
        if i%j==0:
            primo=False
            break
    if primo:
        co+=1
    while num%i==0:
        num=num//i
        cont=cont+1
    if cont>0:
        if desc=="":
            desc="{}^{}".format(i,cont)
        else:
            desc=desc+"*{}^{}".format(i,cont)

print(desc)
print("operaciones=",co)