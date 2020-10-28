lista=[]
for x in range (1,100,3):
    lista.append(x)
print(lista)
del(lista[4:len(lista):3])
print(lista)
print(sum(lista)/len(lista))