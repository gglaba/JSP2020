from itertools import chain 

lista1=[[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
list2=list(chain.from_iterable(lista1))
print(list2)