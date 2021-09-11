tupl1=(57,34,89,(1,2,4),"hello","haiii")
print(tupl1)
print(type(tupl1))
for i in tupl1:
    print(i)

#
# immutable
# keeps order
# support dupication
# hetrogenoius

# nesting possible

tup=1,2,3,4,5,6,7,8,9
print(tup)
print("max value",max(tup))
print("min of tup",min(tup))
print("length of tup",len(tup))
print(tup[0])
print(tup[-1])
print(tup[1:4])