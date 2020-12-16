import random
from timeit import default_timer as timer

lista = []
start=timer()

def genl(ll):
    for _ in range(ll):
        lista.append(random.randint(1,20))
    return lista

def bubble(x):
    n = len(x)
    i = 0
    while(n>1):
        while(i < n-1):
            if(x[i] > x[i+1]):
                x1 = x[i]
                x2 = x[i+1]
                x[i] = x2
                x[i+1] = x1
            i = i+1
        n = n-1
        i=0
    return x

genl(300)
end=timer()
roznica=end-start
print("czas sortowania to: " + str(roznica))
print(bubble(lista))