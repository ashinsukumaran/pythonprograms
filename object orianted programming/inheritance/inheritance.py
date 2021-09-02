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

class Parent(Person):
    def SetPar(self,Parmame,quali):
        self.Parname=Parmame
        self.quali=quali
        print("parent name is ",self.Parname)
        print("qualificatoin is",self.quali)
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
pr=Parent()
pr.setp("ashin",33,"mysore")
pr.SetPar("ajitha","MCA")
