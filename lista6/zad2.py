import szyfrCezara as sz

zdanie = input("Wprowadź zdanie: ")
klucz = int(input("Wprowadź klucz: "))

print(sz.szyfruj(str(zdanie),klucz))
zaszyfr = sz.szyfruj(str(zdanie), klucz)
print(sz.odszyfruj(zaszyfr, klucz))