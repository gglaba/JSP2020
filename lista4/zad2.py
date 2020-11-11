
l=[]
print("wprowadź liczbę elementów")
n=int(input())
for i in range(n):
    print("wprowadź elementy")
    x=(input())
    l.append(x)
setl=set(l)
print(setl)