import itertools
def perm():
        lista=[]
        n=int(input("wprowadź ilość elementów listy: "))
        for n in range(0,n):
            e=int(input("wprowadź elementy listy: "))
            lista.append(e)
            p = list(itertools.permutations(lista))
            print(p)
perm()