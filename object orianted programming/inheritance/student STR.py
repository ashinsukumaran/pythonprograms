class Sudent:
    def __init__(self,name,dept,rollno,collage):
        self.name=name
        self.dept=dept
        self.rollno=rollno
        self.collage=collage
    def print(self):
        print(self.name,self.dept,self.rollno,self.collage)
    def __str__(self):
        return self.name+str(self.rollno)
s=Sudent("ashin","cs",1232,"asas")
s.print()
print(s)

