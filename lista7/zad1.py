from timeit import default_timer as timer

a = int(input("Wprowadz długość ciągu: "))

start=timer()

def fib_iter(n):
    print("0") 
    a = 0
    b = 1
    if n < 0: 
        print("Liczba nie może być mniejsza od 0")
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for _ in range(2,n+1): 
            c = a + b 
            a = b 
            b = c 
            print(a)
        return c

end=timer()
roznica = end - start
fib_iter(a)

print("czas wykonania iteracyjnie: " + str(roznica))

start1 = timer()
def fib_rekur(n):  
   if n <= 1:  
       return n  
   else:  
       return(fib_rekur(n-1) + fib_rekur(n-2))   
if a < 0:  
   print("Liczba nie może być mniejsza od 0")  
else:   
   for i in range(a):  
       print(fib_rekur(i))

end1=timer()
roznica1=end1-start1
print("czas wykonania rekurencyjnie: " + str(roznica1))

