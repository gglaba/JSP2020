N = int(input())
n1, n2 = 0, 1
li = 0
while li < N:
    print(n1)
    nty = n1 + n2
    n1 = n2
    n2 = nty
    li += 1