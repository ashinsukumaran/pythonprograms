# # child class methord overrides parent class methord
# class Person:
#     def print(self,name):
#         self.name=name
#         print("inside person",self.name)
# class Child(Person):
#     def print(self,class1):
#         self.class1=class1
#         print("inside the child",self.class1)
# ch=Child()
# ch.print("abc")


class Calc:
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num2+self.num2)
class Calc2(Calc):
    def add(self,num3,num4):
        self.num3=num3
        self.num4=num4
        print(self.num4-self.num3)
cs=Calc2()
cs.add(12,34)
