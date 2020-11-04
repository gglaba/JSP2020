lista=str((range(100,400))
for x in lista:
    for y in str(x):
        if all ([int(y)]%2==0):
            print(x)