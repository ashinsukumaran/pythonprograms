a=[1,4,11,99,43,5,34,89,2]
# a.sort()
# print(a)
# print(a[0])
# print(a[-1])
min=a[0]
max=a[0]
for i in a:
    if i<min:
        min=i
    elif i>max:
        max=i
print(min)
print(max)


