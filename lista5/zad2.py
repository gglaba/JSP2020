def ntt(liczba):
    lj = ["zero","jeden","dwa","trzy","cztery","pięć","sześć","siedem","osiem","dziewięć","dziesięć","jedenaście","dwanaście","trzynaście","czternaście","pietnaście","szesnaście","siedemnaście","osiemnaście","dziewiętnaście"]
    ld = [ "", "","dwadzieścia","trzydzieści","czterdzieści","pięćdziesiąt","sześćdziesiąt","siedemdziesiąt","osiemdziesiąt","dziewięćdziesiąt"]
    ls = ["", "sto", "dwieście", "trzysta", "czterysta", "pięćset", "sześćset", "siedemset", "osiemset", "dziewięćset"]
    #lt = ["tysiąc"]
 
    if liczba < 20:
        return lj[liczba]

    if liczba < 100:
        list = ([int (i) for i in str(liczba)])
        return ld[list[0]] + " " + lj[list[1]]

    if (liczba > 99):
        list = ([int (i) for i in str(liczba)])
        return ls[list[0]] + " " + ld[list[1]] + " " + lj[list[2]]

print(ntt(73))
