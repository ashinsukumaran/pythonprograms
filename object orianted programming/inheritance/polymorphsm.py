# ploymorphism(many forms)
# overloading------same method name different num of parameters
# overloading ---same method name same number of arguments
#
#
#
# class Person:
#     def show(self,name):
#         self.name=name
#         print("name is ", self.name)
#
#
#
# class Student(Person):
#     def details(self,rollno,mark):
#         self.rollno=rollno
#         self.mark=mark
#         print(self.rollno,self.marks)
#
# st=Student()
# st.details("ashin")
# # st.details(123,54)



class Employee:
    def dispay(self,id,name):
        self.id=id
        self.name=name
        print(self.id,self.name)
class Parent(Employee):
    def dispay(self,age):
        self.age=age
        print(self.age)
p=Parent()
p.dispay(12,34)
# e=Employee()


# class Operators:
#     def num(self,n1,n2):
#         self.n1=n1
#         self.n2=n2
#         print(self.n1+self.n2)
#     def num(self,n3):
#         self.n3=n3
#         print(self.n3)
# np=Operators()
# # np.num(2,5)
# np.num(2)


