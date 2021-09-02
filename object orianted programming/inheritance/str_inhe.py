class Parent:
    def __init__(self,name,adres):
        self.name=name
        self.adres=adres
    def print(self):
        print(self.name,self.age)
class Teacher(Parent):
    def __init__(self,idd,dept,name,adres):
        super().__init__(name,adres)
        self.idd=idd
        self.dept=dept
    def printv(self):
        print(self.idd,self.dept,self.name,self.adres)
    def __str__(self):
        return self.name+str(self.idd)

t=Teacher(1,"ashhh","fsdf","12")
print(t)
t.printv()





