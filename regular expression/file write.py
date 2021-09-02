import re
f2=open('phn','w')
x = x='[L][U][M][0-9]{2}[P][Y][0-9]{3}$'
f1=open("phnw","r")
for i in f1:
    number=i.rstrip("\n")
    match = re.fullmatch(x,number)
    if match!=None:
        f2.write(number)
        f2.write("\n")