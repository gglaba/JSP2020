def ttn():
    x=input("wprowadź liczbę słownie od 1 do 59: ")
    jednosci = {"zero" : '0',"jeden" : '1',"dwa" : '2',"trzy" : '3',"cztery" : '4',"pięć" : '5',"sześć" : '6',"siedem" : '7',"osiem" : '8',"dziewięć" : '9',"dziesięć" : '10',"jedenaście" : '11',"dwanaście" : '12',"trzynaście" : '13',"czternaście" : '14',"piętnaście" : '15',"szesnaście" : '16',"siedemnaście" : '17',"osiemnaście" : '18',"dziewiętnaście" : '19',"dwadzieścia" : '20',"trzydzieści" : '30' ,"czterdzieści" : '40',"pięćdziesiąt" : '50'}
    dziesiatki = {"zero" : '0',"jeden" : '1',"dwa" : '2',"trzy" : '3',"cztery" : '4',"pięć" : '5',"sześć" : '6',"siedem" : '7',"osiem" : '8',"dziewięć" : '9',"dziesięć" : '10',"jedenaście" : '11',"dwanaście" : '12',"trzynaście" : '13',"czternaście" : '14',"piętnaście" : '15',"szesnaście" : '16',"siedemnaście" : '17',"osiemnaście" : '18',"dziewiętnaście" : '19',"dwadzieścia" : '2',"trzydzieści" : '3' ,"czterdzieści" : '4',"pięćdziesiąt" : '5' }
    if len(x.split()) == 1 :
        odp = ''.join(jednosci[i] for i in x.split())
    if len(x.split()) > 1 :
        odp = ''.join(dziesiatki[i] for i in x.split())
    print(odp)
ttn()
     