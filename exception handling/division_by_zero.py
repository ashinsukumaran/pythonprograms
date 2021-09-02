n1=int(input("number 1"))
n2=int(input("number 2"))
try:
    print(n1/n2)
except Exception as e:
    print(e.args)
