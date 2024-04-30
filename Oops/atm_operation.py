class Atm:
    pin=1227
    Account_no=934548153
    balance=1500
    def __init__(self):
        self.pin=self.pin
        self.Account_no=self.Account_no
        self.balance=self.balance
        print("Hello customer")

class operation(Atm):
    def withdraw(self,new_pin,Amount):
        if new_pin==self.pin:
            self.balance=self.balance-Amount
            print("balance",self.balance)
        else:
            print("Invalid pin")
            
    def deposit(self,new_account,Amount):
        if new_account==self.Account_no:
            self.balance=self.balance+Amount
            print("Balance:",self.balance)
        else:
            print("invalid Account number")
    
    def mini_statement(self,pin):
        if self.pin==pin:
            print("Account Number:",self.Account_no)
            print("Balance",self.Account_no)
        else:
            print("Invalid pin")
    
    def enquiry(self,pin):
        if self.pin==pin:
            print("Current balance:",self.balance)
            print("Allow to withdraw",self.balance-500)
        else:
            print("Invalid pin")
            
# obj1=Atm()
obj2=operation()

while True:
    print("Choose: withdraw(1),Deposit(2),Mini_statement(3),Enquiry(4),exit(5)")
    met=input()
    if met=="1":
        print("Pin:")
        x=int(input())
        print("Amount:")
        y=int(input())
        obj2.withdraw(x,y)
    elif met=="2":
        print("Account no:")
        x=int(input())
        print("Amount:")
        y=int(input())
        obj2.deposit(x,y)
    elif met=="3":
        print("Enter pin:")
        pin=int(input())
        obj2.mini_statement(pin)
    elif met=="4":
        print("Enter pin:")
        pin=int(input())
        obj2.enquiry(pin)
    elif met == "5":
        break
    else:
        print("Choose valid input")