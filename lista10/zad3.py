from itertools import combinations

class Kombinacje():
    def __init__(self,lista):
        self.lista=lista
    def podlisty(self):
        podlisty=[]
        for i in range(len(self.lista)+1):
            podlista=[]
            for j in combinations(self.lista,i):
                if len(j)==3 and sum(j)==0 :
                    podlista.append(j)
            podlisty.extend(podlista)
        return podlisty

t1=Kombinacje([-5,-3,2,-1,0,5,4,7,3])
t2=t1.podlisty()
print(t2)
