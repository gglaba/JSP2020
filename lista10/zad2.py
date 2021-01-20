from itertools import combinations

class Kombinacje():
    def __init__(self,lista):
        Kombinacje.lista=lista
    def podlisty(self):
        podlisty=[]
        for i in range(len(self.lista)+1):
            podlista=[]
            for j in combinations(self.lista,i):
                podlista.append(j)
            podlisty.extend(podlista)
        return podlisty

t1=Kombinacje([1,2,3])
t2=t1.podlisty()
print(t2)
