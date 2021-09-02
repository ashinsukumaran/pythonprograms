print("odd or even program with functions without arguments")
def odd_even():
    num=int(input("enter a number"))
    if num>0:
        if num % 2 == 0:
            print("nuber is even", num)

        else:
            print("number is odd", num)
    elif num==0:
        print("number is 0")
    else:
        print("the number is a -ve number")
odd_even()
odd_even()