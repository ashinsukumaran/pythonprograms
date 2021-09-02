class Person:
    def setvalue(self,name,age):
        self.name=name
        self.age=age
    def printvalue(self):
        print("name",self.name)
        print("age",self.age)
p1=Person()
p1.setvalue("ashin",27)
p1.printvalue()