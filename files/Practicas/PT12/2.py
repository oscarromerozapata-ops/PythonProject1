#Converteix la llista a=[1,[2,[3,4]],5] en [1,[2,[3, 4],[6,7]], 5].
a=[1,[2,[3,4]],5]
a[1].append([6,7])
print(a)