class Vehicle:
    def details(self,model,color,regnumber):
        self.model=model
        self.color=color
        self.regnumber=regnumber
        print("model is ", self.model)
        print("color is ", self.color)
        print("regnumber is ", self.regnumber)

class Bus(Vehicle):
    def print(self,name,owner):
        self.name=name
        self.owner=owner
        print(self.name,self.owner)

bus=Bus()
bus.details(2020,"red","kl58ae1243")
bus.print("ash","ashin")
