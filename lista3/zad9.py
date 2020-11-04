print("Wprowadź liczbę wierszy: ")
m=int(input())
print("Wprowadź liczbę kolumn: ")
n=int(input())
for x in range(m):
     for y in range(n):
         print (x*y, end="\t")
     print()