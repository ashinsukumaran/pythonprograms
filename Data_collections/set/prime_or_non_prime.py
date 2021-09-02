sett={1,2,3,4,5,6,7,8,9}
prime=set()
notprime=set()
for i in sett:
    if i >= 1:
        for j in range(2, i):
            if (j % i) == 0:
                notprime.add(i)
                break
        else:
            prime.add(i)
print(prime)
print(notprime)
