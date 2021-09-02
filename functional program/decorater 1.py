def admin_required(func):
    def wrapper(a,b):
        if a!="admin":
            raise Exception("you are not allowed")
        else:
            return func(a,b)
    return wrapper
@admin_required
def chnagepin(user,pin):
    mypin=pin
    return mypin
@admin_required
def delet_ac(user,acno):
    return str(acno)+" deleted"
# print(chnagepin("admin",1000))
print(delet_ac("admin", 2000))
