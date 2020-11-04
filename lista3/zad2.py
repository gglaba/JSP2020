print("wprowadź liczbę całkowitą: ")
x=input()
if int(x)%2==0:
    print(x + " jest liczbą parzystą")

elif int(x)%2 != 0:
    print(x + " jest liczbą nieparzystą")

y=input()
l=["liczba parzysta","liczba nieparzysta"][int(y)%2]
print(l)


