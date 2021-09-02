# class Student:
#     def details(self,name,age,std):
#         self.name=name
#         self.age=age
#         self.std=std
#
#
#     def display(self):
#         print(self.name,self.age,self.std)
# S=Student()
# S.details("ashin",23,12)
# S.display()


class Student:
    school="Amrita"
    def details(self, name, age, std):
        self.name = name
        self.age = age
        self.std = std

    def display(self):
        print(self.name, self.age, self.std,Student.school)
S = Student()
S.details("ashin", 23, 12)
S.display()