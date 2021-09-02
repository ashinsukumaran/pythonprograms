class Emp:
    def __init__(self,name,age,designation,company):
        self.name=name
        self.age=age
        self.designation=designation
        self.company=company
    def display(self):
        print("name is ",self.name)
        print("age is ",self.age)
        print("designation is",self.designation)
        print("company is",self.company)
obj =Emp("ashin",23,"webdeveloper","venteck solutions")
obj.display()