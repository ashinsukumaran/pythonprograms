# class Bank:
#     def account(self,accno,name,age,phone):
#         self.accno=accno
#         self.name=name
#         self.age=age
#         self.phone=phone
#     def deposite(self,amount,type):
#         self.amount=amount
#         self.type=type
#     def withdraw(self,balace):
#         self.balance=balace
#     def dispay(self):
#         print("accno",self.accno)
#         print("name",self.name)
#         print("age",self.age)
#         print("phone",self.phone)
#         print("amount",self.amount)
#         print("balace",self.balance)
#
# b=Bank()
# b.account(123,"ashin",27,8943693868)
# b.withdraw(5000)
# b.deposite(2000,"savings")
# b.dispay()


class Bank:
    bname="Sbi"
    def create(self,accno,name):
        self.accno=accno
        self.name=name
    def deposite(self,amt,balace):
        self.amt=amt
        self.balace+=self.amt
        print("your ",Bank.bname,"account has been credited with amt",self.amt)
        print("your curent balance is ",self.balance)
    def withdraw(self,amnt):
        self.amnt=amnt
        if self.amnt > self.balance:
            print("insssufficient balance")
        else:
            print("account credited with",self.amnt)
            self.balance-=self.amnt
            print("avalable balance",self.balance)
obj=Bank()
obj.create(111,"ashin")
obj.deposite(1200,200)
obj.withdraw(200)