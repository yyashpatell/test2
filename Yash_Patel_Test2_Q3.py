class Account():
    def __init__(self):
        self.balance=0
        print("your current balance is:", self.balance)
print("hello!!! welcome to the deposit and withdrawal machine")


withdrawal = 1
deposit = 2
method = input("for withdrawal enter 1 and for deposit enter 2:")

if method == 1:

    def withdrawal(self):
        amount = float(input("enter amount to be with drawn:"))
        if self.balance >= amount:
           self.balance= self.balance - amount
        print("\n amount withdrawn: %f" % self.balance)
else:
            print("insufficient balance")
            
    
if method == 2:
        
    def deposit(self):
        amount =float(input("enter amount to be deposited:"))
        self.balance = self.balance + amount
        print("\n amount deposited:%f" % self.balance)


def display(self):
        print("\n net available balance= %f" % self.balance)

s= Account()
s.deposit()
s.withdrawal()
s.display()


