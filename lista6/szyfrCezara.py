litery = 'abcdefghijklmnopqrstuvwxyz'

def szyfruj(zdanie, klucz):
    zaszyfr = ""
    for i in zdanie:
        if(i in litery):
            char = i
            zaszyfr += chr((ord(char) + klucz - 97 ) % 26 +97)
    return zaszyfr

def odszyfruj(zdanie, klucz):
    odszyfr = ""
    for i in zdanie:
        if(i in litery):
            char = i
            odszyfr += chr((ord(char) - klucz - 97) % 26 +97)
    return odszyfr