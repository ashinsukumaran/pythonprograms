def printval(*args):
    return (args)
print(printval(2,4,6,9,0))
# args output i tuple


def details(**args):
    return args
print(details(name="ashin",age=27,place="kannur"))
# **args output in dict