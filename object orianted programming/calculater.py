class Calc:
    res=0
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2
        res=self.num1+self.num2
        print(res)
    def sub(self,num1,num2):
        res=self.num1-self.num2
        print(res)
    def mult(self,num1,num2):
        res=self.num1*self.num2
        print(res)
    def div(self,num1,num2):
        res=self.num1/self.num2
        print(res)
obj=Calc()
obj.add(12,34)
obj.sub(2,2)
obj.mult(2,5)
obj.div(4,2)


