import math
print("wprowadź współczynnik a")
a=float(input())
print("wprowadź współczynnik b")
b=float(input())
print("wprowadź współczynnik c")
c=float(input())
delta= (b**2) - (4 * a * c)
if a==0 :
    print("to nie jest równanie kwadratowe")
elif delta==0 :
    x0= (-b)/(2*a)
elif delta>0 :
    x1 = (-b-math.sqrt(delta))/(2*a)
    x2 = (-b+math.sqrt(delta))/(2*a)
    print("x1= " + str(x1) + " x2= " + str(x2))
elif delta<0:
    print("to równanie nie ma rozwiązań")