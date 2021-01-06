import os
from datetime import datetime
import szyfrCezara as sz


path = input("Wprowadz sciezke: ")
key = int(input("Wprowadz klucz do szyfrowania: "))
data=datetime.today().strftime('%Y-%m-%d')


def tkatalog(zaszyfr):
    zapis = input("ścieżka zapisu: ")
    try:
        os.makedirs(zapis)
        os.chdir(zapis)
        nazwa= "plik_zaszyfrowany_" + str(key) + "_" + str(data) + ".txt"
        plik = open(nazwa,"w+")
        plik.write(zaszyfr)
        return 1
    except IOError:
        print("Ścieżka istnieje!")

def zamianatekst(path):
    plik = open(path, "r")
    plik1 = plik.read()
    tkatalog(sz.szyfruj(plik1, key))


zamianatekst(path)
