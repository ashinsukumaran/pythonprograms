class person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def printval(self):
        print(self.name,self.age,self.address)
obj=person("ashin",27,"abc")
obj.printval()