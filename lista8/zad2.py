import os
from datetime import datetime
import szyfrCezara as sz

path = input("Wprowadz sciezke: ")
data=datetime.today().strftime("%Y-%m-%d")

def klucz():
    p=os.path.split(path)
    p1 = str(p[1])
    l1=p1[18]
    try:
        l2=int(p1[0][19])
        key=str(l1) + str(l2)
    except Exception:
        key=l1
    return key

key = klucz()

def tkatalog(odszyfr):
    zapis = input("ścieżka zapisu: ")
    try:
        os.makedirs(zapis)
        os.chdir(zapis)
        nazwa = "plik_deszyfrowany_" + str(key) + "_" + str(data) + ".txt"
        plik = open(nazwa,"w+")
        plik.write(odszyfr)
        return 1
    except IOError:
        print("Ścieżka istnieje!")


def zamianatekst(path):
    plik = open(path, "r")
    plik1 = plik.read()
    tkatalog(sz.odszyfruj(plik1, int(key)))

zamianatekst(path)