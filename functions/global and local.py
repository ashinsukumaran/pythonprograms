x=10
a=4
def foo():
    # x=3
    global x,a
    x+=10
    print("local x is ",x)
foo()
print("global x is ",x)