class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printVal(self):
        print("name",self.name)
        print("age",self.age)
class Dog(Animal):
    def __init__(self,color,size,name,age):
        super().__init__(name,age)
        self.color=color
        self.size=size
    def printVal(self):
        print(self.color)
        print(self.size)
        print(self.name)
        print(self.age)
dog=Dog("black","medium","appu",4)
dog.printVal()