import random
from timeit import default_timer as timer

lista = []
start=timer()
def bubble(x):
    n = len(x)
    i = 0
    while(n>1):
        while(i < n-1):
            if(x[i] > x[i+1]):
                zas = x[i]
                zas2 = x[i+1]
                x[i] = zas2
                x[i+1] = zas
            i = i+1
        n = n-1
        i = 0
    return x


def sort(len):
    for _ in range(len):
        lista.append(random.randint(1,20))
    return lista

sort(100)
end=timer()
roznica=end-start
print("czas sortowania to: " + str(roznica))
print(bubble(lista))