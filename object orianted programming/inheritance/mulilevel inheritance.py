# class A:
#     def printA(self):
#         print("inside A")
# class B(A):
#     def printB(self):
#         print("inside B")
# class C(B):
#     def printC(self):
#         print("inside C")
# a=A()
# a.printA()
# b=B()
# b.printA()
# b.printB()
# c=C()
# c.printA()
# c.printB()
# c.printC()



class Person:
    def setp(self,name,age,adds):
        self.name=name
        self.age=age
        self.adds=adds
        print("name is ", self.name)
        print("age is ", self.age)
        print("adds is ", self.adds)
class Child(Person):
    def setc(self,div,school):
        self.div=div
        self.school=school
        print("div is",self.div)
        print("school is ",self.school)
class Student(Child):
    def setS(self,rollno,marks):
        self.rollno=rollno
        self.marks=marks
        print("rollno is ",self.rollno)
        print("marks are",self.marks)

p=Person()
s=Student()
s.setp("ashin",2,"kannur")
s.setc("mca","asas")
s.setS("mca121",234)
