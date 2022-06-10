class Account:
    Account="PostBank"
    def __init__(self,account_number,account_name,):
        self.account_name=account_name
        self.account_number=account_number
        self.balance=0
        self.deposits=[]
        self.withdrawal=[]
        self.transaction_fee=100

    def deposit(self,amount):
        if amount<=0:
            return f"Deposit should be positive amount"
        else:
          self.balance+=amount
          self.deposits.append(amount)
        return f"hello {self.account_name} you have deposited {amount} and you new balance is {self.balance}"  


    def withdraw(self,amount):
        total=amount+self.transaction_fee
        if amount<=0:
            return f"withdraw should be greater than zero"
        elif amount>self.balance:
            return f"your balance is {self.balance} you can't withdraw {amount}"    
        else: 
         self.balance-=total
        self.withdrawal.append(amount)
        return f"hello {self.account_name} you have withdrawn {amount} your new balance is {self.balance}"  
    
    def deposit_statement(self):
        for b in self.deposits:
            print(b, end="\n")
    
    def withdrawals_statement(self):
        for withdrawal in self.withdrawal:
            print(withdrawal,end="\n")

    def account_balance(self):
       return f"Hello your account balance is {self.balance}"       

