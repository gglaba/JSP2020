import matplotlib.pyplot as plt
import numpy as np

nazwa = ["C", "Java", "Python", "C++", "C#", "VisualBasic", "JS", "PHP",
         "R", "Groovy"]
pktprocent = [17.38,11.96,11.72,7.56,3.95,3.84,2.20,1.99,1.9,1.84]

def wykres():
    plt.bar(np.arange(10), pktprocent,color="green")
    plt.ylabel("Popularność w %")
    plt.xlabel("Język programowania")
    plt.xticks(np.arange(10), nazwa,fontsize=8)
    plt.title("10 najpopularniejszych języków programowania")
    plt.show()

wykres()