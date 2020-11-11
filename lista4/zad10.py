
def nwd(x,y):
    d=x%y
    while d:
        x=y
        y=d
        d=x%y
    print(y)
nwd(60,18)