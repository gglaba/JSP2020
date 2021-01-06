import random
import os

def pesel():

    rok = random.randint(1900,2099)

    if rok <= 1999:
        mies = random.randint(1,12)

    elif rok >= 2000:
        mies = random.randint(1,12) + 20 

    nparz = (1, 3, 5, 7, 8, 10, 12, 21, 23, 25, 27, 28, 30, 32)
    parz = (4, 6, 9, 11, 24, 26, 29, 31)

    if mies in nparz:
        dzien = random.randint(1,31)

    elif mies in parz:
        dzien = random.randint(1,30)		
    else:
        if rok % 4 == 0 and rok != 1900:
            dzien = random.randint(1,29) 
        else:
            dzien = random.randint(1,28) 

    seria = str(random.randint(1000,9999))

    r = '%02d' % (rok % 100)
    m = '%02d' % mies
    dd = '%02d' % dzien

    a = int(r[0])
    b = int(r[1])
    c = int(m[0])
    d = int(m[1])
    e = int(dd[0])
    f = int(dd[1])
    g = int(seria[0])
    h = int(seria[1])
    i = int(seria[2])
    j = int(seria[3])
    
    spr = a + 3 * b + 7 * c + 9 * d + e + 3 * f + 7 * g + 9 * h + i + 3 * j

    if spr % 10 == 0:
        ostatnia = 0
    else:
        ostatnia = 10 - (spr % 10)

    l1 = ('%02d' % (rok % 100))
    l2 = ('%02d' % mies)
    l3 = ('%02d' % dzien)
    l4 = (seria)
    l5 = (ostatnia)

    return (str(l1)+str(l2)+str(l3)+str(l4)+str(l5))

plik = open("PESEL.txt","w+")

for _ in range (10):
    plik.write(str(pesel()) + '\n')