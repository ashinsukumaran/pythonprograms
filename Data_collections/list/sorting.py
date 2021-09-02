my_list=[1,4,11,99,43,5,34,89,2]

new_list=[]
while my_list:
    min= my_list[0]
    for i in my_list:
        if i<min:
            min=i
    new_list.append(min)
    my_list.remove(min)

print(new_list)
print(my_list)