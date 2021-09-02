a=[1,4,11,99,43,5,34,89,2]
def bsearch():
    a.sort()
    print(a)
    ele=int(input("enter element"))
    low=0
    fla=0
    upp=len(a)-1
    while low<= upp:
        mid = (low+upp)//2
        if ele >a[mid]:
            low=mid+1
        elif ele< a[mid]:
            upp=upp-1
        elif ele==a[mid]:
            flag=1
            break
    if flag==1:
        print("found")
    else:
        print("not found")

bsearch()