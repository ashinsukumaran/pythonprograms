class Person:
    def details(self,name,age,number):
        self.name=name
        self.age=age
        self.number=number
    def display(self):
        print("name is ",self.name)
        print("age is ",self.age)
        print("number is ", self.number)
class Employee(Person):
    def set(self,id,salary,dept):
        self.id=id
        self.salary=salary
        self.dept=dept
        print(self.id,self.salary,self.dept)
    print("employee class")
p=Person()
p.details("ashin",23,8943593498)
p.display()
e=Employee()
e.details("raju",23,54343442423)
e.set(22,100000,"cs2xd")
e.display()