class Vehicle:
    def __init__(self,model,regno,color):
        self.model=model
        self.regno=regno
        self.color=color
    def print(self):
        print("model is",self.model)
        print("regno is",self.regno)
        print("color is ",self.color)
    def __str__(self):
        return self.model+ self.color
v=Vehicle("Honda DIO DLX 2020","KL581347","RED")
v.print()
print(v)