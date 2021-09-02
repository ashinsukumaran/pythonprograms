class Addion:
    def Add(self,value1,value2):
        self.value1=value1
        self.value2=value2
    def res(self):
        result=self.value1+self.value2
        print("Addition      of",self.value1,"and",self.value2,"is",result)
a=Addion()
a.Add(12,23)
a.res()