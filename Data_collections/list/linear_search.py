lst = [1,2,4,5,6,7,8,3,33,45,64,56,34,67,34,98,23,46,38,389,23,87]
def linear_search(lst):
    n=int(input("enter the element"))
    fla=0
    for i in  lst:
        if i==n:
            fla=1
            break
    if fla==0:
        print("not found")
    else:
        print("present")
linear_search(lst)