class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printv(self):
        print("name", self.name)
        print("age", self.age)
class Employee(Person):
    def __init__(self, id, salary,name, age):
        super().__init__(name, age)
        self.id=id
        self.salary=salary
    def print(self):
        print(self.id)
        print(self.salary)
        print(self.name)
        print(self.age)
em=Employee(12,2344,"ashin",32)
em.print()
em.printv()
