class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printv(self):
        print("name is",self.name)
        print("age is",self.age)

f1=open("student",'r')
for line in f1:
    l=line.split(",")
    name=l[0]
    age=l[1]
    st=Student(name,age)
    print(st)
    st.printv()