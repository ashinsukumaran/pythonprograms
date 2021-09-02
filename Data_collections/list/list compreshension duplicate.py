int_list = [1,0,7,5,9,2,3,5,7,2,0,1,10]
temp = []
[temp.append(x) for x in int_list if x not in temp]
print(temp)