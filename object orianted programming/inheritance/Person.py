# multiple inheritance
class Person:
    def details(self,name,age,number):
        self.name=name
        self.age=age
        self.number=number
        print("name is ", self.name)
        print("age is ", self.age)
        print("number is ", self.number)

class Child:
    def set(self,school,std):
        self.school=school
        self.std=std
        print(self.school,self.std)
class Student(Person,Child):
    def printv(self,rollno,mark):
        self.rollno=rollno
        self.mark=mark

st=Student()
st.details("ashin",12,2445255)
st.printv(123,54)
st.set("asas",2)

p=Person()
p.details("ashin",23,8943593498)

