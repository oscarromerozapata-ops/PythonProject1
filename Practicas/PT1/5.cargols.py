cond=0
defectuosos=200
produits=10000

if defectuosos<200:
    if produits>10000:
        cond=8
    else:
        cond=6
elif produits<10000:
    if defectuosos>200:
        cond=7
    else:
        cond=5
print("GRAU",cond)