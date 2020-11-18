slw = input("słowa do zaszyfrowania: ")
klucz = {'a': 'y', 'e' : 'i', 'i' : 'o', 'o' : 'a', 'y': 'e'}
def szyfr(slw, klucz):
    for item in slw:
        if item in klucz.keys():
            slw = slw.replace(item, klucz[item])
    return slw

def reszyfr(slw, klucz):
    reverse_klucz = dict(map(reversed, klucz.items()))
    for item in slw:
        if item in reverse_klucz.items():
            slw = slw.replace(item, reverse_klucz[item])
    return slw

print(szyfr(slw, klucz))
print(reszyfr(slw, klucz))