fixed_amount = 10000
withdraw_amount = int(input("enter the amount"))
if fixed_amount>=withdraw_amount:
    balance=fixed_amount-withdraw_amount
    print("balance amount is", balance)
else:
    print("insufficient balance")
