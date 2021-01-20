import os
import datetime

def poprawnosc(numer):
    wspol = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)
    sprawdz = sum(w * int(n) for w, n in zip(wspol, numer))
    if str((10 - sprawdz) % 10) == numer[10]:
        return 1
    else:
        return 0

def uro(numer):
    rok = int(numer[0:2])
    mies = int(numer[2:4])
    dzien = int(numer[4:6])
    rok += {
        0: 1900,
        1: 2000,
        2: 2100,
        3: 2200,
        4: 1800,
    }[mies // 20]
    mies = mies % 20
    try:
        return datetime.date(rok, mies, dzien)
    except ValueError:
        return 0

def plec(numer):
    if numer[9] in '02468': 
        return 'K'
    else:
        return 'M'

def sprawdzpsl(string):
    for x in range (len(string)):
        print (x)

def mdir(wart):
    f = open("PESELDSZFR.txt","w+")
    f.write(wart)

def zamianastr(path):
    zero = 0
    ost = 11
    wart = ""
    deszyfr = ""
    f = open(path, "r")
    f1 = f.readlines()
    for x in f1:
        deszyfr += x
    for x in range (10):
        if(poprawnosc(deszyfr[zero:ost]) == 1):
            wart += deszyfr[zero:ost] + " " + plec(deszyfr[zero:ost]) + " " + str((uro(deszyfr[zero:ost]))) + '\n'
            mdir(wart)
        else:
            print("Niepoprawny numer PESEL")
        zero += 12
        ost += 12

zamianastr("PESEL.txt")