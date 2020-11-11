
lista=[]
print("wprowadź ilość elementów listy")
n=int(input())
for i in range(0,n):
    print("wprowadź elementy listy")
    e=int(input())
    lista.append(e)
def iloczyn(l):
    wynik=1
    for x in l:
        wynik=wynik * x
    return wynik
print("Suma listy - 0,Iloczyn listy - 1,Suma i iloczyn - 3")
d=int(input())
if d == 0:
    print(sum(lista))
elif d == 1:
    print(iloczyn(lista))
elif d == 3:
    print("iloczyn= " + str(iloczyn(lista)) + " suma= " + str(sum(lista)))
else:
    print("Niepoprawna liczba!")
