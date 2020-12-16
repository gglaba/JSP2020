import random
from timeit import default_timer as timer

lista = []
start=timer()

def genl(ll):
    for _ in range(ll):
        lista.append(random.randint(1,20))
    return lista

def sort(a): 
    for i in range(1, len(a)):
        klucz = a[i]  
        
        while i-1 > 0 and a[i-1] > klucz: 
            a[i] = a[i-1] 
            i=i-2
        a[i] = klucz 
    return a

end=timer()
roznica=end-start
genl(300)
print(sort(lista))
print("czas działania programu: " + str(roznica))