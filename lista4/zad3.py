import math
#def converter():
 #   x=int(input("zamiana rad->deg (1) , zamiana deg->rad (0):  "))
  # if x == 1:
   #     y=float(input("wprowadź rad:  "))
   #     y=y*(180/math.pi)
    #    print(y)
    #if x == 0:
     #   y=float(input("wprowadź deg:  "))
      #  y=y*(math.pi/180)
       # print(y)
#converter()

def konw(degtorad=1,radtodeg=1):
    degtorad=degtorad*(math.pi/180)
    radtodeg=radtodeg*(180/math.pi)
    print("stopnie na radiany: " + str(degtorad) + " radiany na stopnie: " + str(radtodeg))
konw(90,50)

