import math

def spr(a,b,c):
    if a+b>c and a+c>b and b+a>c:
        return("warunek trójkąta spełniony")
    else:
        return("to nie jest trójkąt")
def obw(a,b,c):
    L=a+b+c
    return(L)
def pole(a,b,c):
    hl=((a+b+c)/2)
    P=math.sqrt(hl*(hl-a)*(hl-b)*(hl-c))
    return(P)
def rodzaj(a,b,c):
    if a == b and a == c:
        return("trójkąt równoboczny")
    elif a == b or b == c or a == c:
        return("trójkąt równoramienny")
    else:
        return("trójkąt różnoboczny")
def kat(a,b,c):
    if c*c > a*a + b*b:
        return("trójkąt rozwartokątny")
    elif c*c == a*a + b*b:
        return("trójkąt prostokątny")
    else:
        return("trójkąt ostrokątny")
