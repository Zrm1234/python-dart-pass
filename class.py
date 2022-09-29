#parant class
class Account():
    def __init__(self,accountNo,name,dateOfBrith,amount,DateTime):
        self.accountNO = accountNo
        self.name = name
        self.dateOfBrith = dateOfBrith
        self.amount = amount
        self.DateTime = DateTime

    def insert(self):
        print("the deatils of the user")
        print("the acontc : ", self.accountNO)
        print("the name", self.name)
        print("the dateOfBrith :", self.dateOfBrith)
        print("the amount :", self.amount)
        print("the DateTime",self.DateTime)
        
    
    def deposit(self,amount):
        self.balance = 0
        self.amount = amount
        self.balance = self.balance + amount
        print("the amount has been updated : $",self.balance)

    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("account has been updated : $",self.balance)
        else:
            print(self.balance)
    def checkBalance(self):
        self.balance = balance
        print("the detalis of balance",self.balance)

user1 = Account(1, "zahraa", "2003", "1000$", "2010"),
user2 = Account(2, "Aya", "2002", "500$", "2006"),
user3 = Account(3, "Ahmed", "2005", "300$", "2002")
user1.insert()
user1.deposit(100)
user1.withdraw(50)
user1.checkBalance()
    


    






