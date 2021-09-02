# class Employee:
#     def setvalue(self,id,name,age,company,salary,department):
#         self.id=id
#         self.name=name
#         self.age=age
#         self.company=company
#         self.salary=salary
#         self.department=department
#     def printvalue(self):
#         print("id",self.id)
#         print("name",self.name)
#         print("age",self.age)
#         print("company",self.company)
#         print("salary",self.salary)
#         print("department",self.department)
# E=Employee()
# E.setvalue(1,"ashin",27,"veniteck",2000,"web")
# E.printvalue()



class Employee:
    company="veniteck solutions"
    def setvalue(self,id,name,age,salary,department):
        self.id=id
        self.name=name
        self.age=age
        self.salary=salary
        self.department=department
    def printvalue(self):
        print("id",self.id)
        print("name",self.name)
        print("age",self.age)
        print("company",Employee.company)
        print("salary",self.salary)
        print("department",self.department)
E=Employee()
E.setvalue(1,"ashin",27,2000,"web")
E.printvalue()