print("list program to enter elements and store it in a list")
l=[]
n=int(input("enter the size of the list"))
for i in range(n):
    e=int(input("enter the elements"))
    l.append(e)
print("elements in list are",l)
