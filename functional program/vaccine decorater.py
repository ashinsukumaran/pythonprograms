def vaccinater(func):
    def wrapper(name,age,place):
        if age<18:
            raise Exception("you are not allowed")
        else:
            return func(name,age,place)
    return wrapper
@vaccinater
def vaccine(name,age,place):

    return ("elegible")

print(vaccine("ashin",27,"thalassery"))


