class Person:
    def set(self,name,age,num):
        self.name=name
        self.age=age
        self.num=num
        print(self.name,self.age,self.num)
class Parent(Person):
    def setP(self,edu,adrs):
        self.edu=edu
        self.adrs=adrs
class Employee(Parent):
    def setE(self,id,salary):
        self.id=id
        self.salary=salary

e=Employee()
e.set("ash",23,4432432)
e.setE(12,242423)
e.setP("bca",543)