import math

class Kolo:
    def __init__(self,r):
        self.r = r
    def pole(self):
        return ("Pole: " + str(self.r * self.r * math.pi))
    def obwod(self):
        return ("Obwód: " + str(2 * math.pi * self.r))
    
p1=Kolo(10)
p2=p1.pole()
p3=p1.obwod()
print(p2)
print(p3)