a = [1,2,4,5,6,7,8,3,33,45,64,56,34,67,34,98,23,46,38,389,23,87]
b=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        print(i)


