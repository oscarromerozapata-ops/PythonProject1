num=int(input("Quants números vas a introduir?"))
n=""
c=0
for i in range(num):
    n=int(input(f"Dona'm el número {i+1}: "))
    if n<0:
        c+=1
print("Has escit",c,"numeros negatius")
