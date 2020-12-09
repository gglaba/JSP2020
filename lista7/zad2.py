import random
from timeit import default_timer as timer

lista = []
start=timer()
def sort(x): 
    for i in range(1, len(x)):
        klucz = x[i]  
        j = i-1
        while j >=0 and x[j] > klucz: 
            x[j+1] = x[j] 
            j -= 1
        x[j+1] = klucz 
    return x


def gen(l):
    for _ in range (l):
        lista.append(random.randint(1, 20))
    return lista

end=timer()
roznica=end-start
gen(300)
print(sort(lista))
print("czas działania programu: " + str(roznica))