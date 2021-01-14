import sys
import numpy as np

def system(arg):
    l = list()
    l = [int(x) for x in arg.split(',')]
    return l

def plik(arg):
    l = list()
    with open(arg) as dane:
        for i in dane:
            i = i.replace("\n", "")
            l.append(int(i))
    return l

def obliczenia(arg):
    print(" Średnia: " + str(np.average(arg)) + "\n Odchylenie standardowe: " + str(np.std(arg)) + "\n Wariancja: " + str(np.var(arg)))

if ".txt" in sys.argv[1]:
    obliczenia(plik(sys.argv[1]))
else:
    obliczenia(system(sys.argv[1]))