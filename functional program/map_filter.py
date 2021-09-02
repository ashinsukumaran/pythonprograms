from _functools import reduce
lst=[2,3,4,5,6]

######################### map functions start
# cubes=list(map(lambda num:num**3,lst))
# print(cubes)
#
# squares=list(map(lambda  num:num**2,lst))
# print(squares)

########################map functions end


# ######################filter functoin start

# evens=list(filter(lambda num:num%2==0,lst))
# print(evens)

# odds=list(filter(lambda num:num%2 !=0,lst))
# print(odds)
# ###################filter functoin end



#------------------------ reduce function start


# low=reduce(lambda num1,num2:num1 if num1<num2 else num2,lst)
# print(low)

large=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print(large)

#------------------------ reduce function end