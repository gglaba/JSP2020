spolgloski=["b","c","ć","d","f","g","h","j","k","l","ł","m","n","p","r","s","t","w","z","ż","ź"]
samogloski=["a","ą","e","ę","i","o","u","y"]
print("wprowadź literę: ")
x=input()
if x in samogloski:
     print(x + " jest samogłoską")
elif x in spolgloski:
    print(x + " kjest spółgłoską") 
