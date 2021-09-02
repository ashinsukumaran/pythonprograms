class Student:
    def __init__(self,name,id,course,mark):
        self.name=name
        self.id=id
        self.course=course
        self.mark=mark

    def printv(self):
        print("name is",self.name)
        print("name is", self.id)
        print("name is", self.course)
        print("age is",self.mark)

f1=open("student1",'r')
for line in f1:
    l=line.split(",")
    name=l[0]
    id=l[1]
    course=l[2]
    mark=l[3]
    st=Student(name,id,course,mark)
    print(st)
    st.printv()