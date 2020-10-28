list=["Kasia","Basia","Marek","Darek"]
list.append("Józek")
lista2=["Ania","Basia"]
list.extend(lista2)
list.sort()
print(list[3])
print(list[0:2])
print(list[5:])
while "Basia" in list:
    list.remove("Basia")  
print(list)
print(len(list))
tuple=(list)
print(list)