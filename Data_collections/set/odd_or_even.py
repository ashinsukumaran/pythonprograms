
a = set()
num=int(input("enter size of set "))
for i in range (num):
    n = int(input("enter numbers"))
    a.add(n)
# a={8,1,3,65,8,9,0,3}
even = set()
odd = set()
for i in a:
 if i%2==0:
     even.add(i)
 else:
    odd.add(i)
print(even)
print(odd)

