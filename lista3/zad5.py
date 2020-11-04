import re
x=input()
a=re.search("[a-zA-Z]",x)
b=re.search("[0-9]",x)
c=re.search("[@#$]",x)
print(a)
print(b)
print(c)