

a={1,2,3,4,5,6}
b={3,4,5,6,7,8,9,10}
c=set()
for i in a:
    if i in b:
        c.add(i)
    # for j in b:
    #     if i==j:
    #         c.add(i)
print(c)