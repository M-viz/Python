class Category:
    def __init__(self,category):
        self.category=category
        self.ledger=[]

    def __str__(self):
        title = f'{self.category.center(30, "*")}\n'
        total= f'Total: {self.get_balance()}'
        entries=''
        for entry in self.ledger:
            des= entry["description"][:23].ljust(23)
            amt= f'{str("{:.2f}".format(float(entry["amount"]), 2)).rjust(7)}'
            entries+= f'{des}{amt}\n'
        return title+entries+total

    def deposit (self,amount,description=''):
        positive_amount=abs(amount)
        self.ledger.append({"amount": positive_amount, "description": description})

    def withdraw (self,amount,description=''):
        if self.check_funds(amount):
            negative_amount=abs(amount)*-1
            self.ledger.append({"amount": negative_amount, "description": description})
            return True
        else: 
            return False

    def get_balance(self):
        current_balance=0
        for entry in self.ledger:
            current_balance += entry["amount"]
        return current_balance
    
    def get_balance_withdraw(self):
        withdraw_balance=0
        for entry in self.ledger:
            if entry["amount"] < 0:
                withdraw_balance += entry["amount"]
        return withdraw_balance
    
    def transfer(self,amount,category):
        if self.check_funds(amount):
            self.withdraw(amount,f'Transfer to {category.category}')
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        else:
            return False
        
    def check_funds(self,amount):
        if amount > self.get_balance(): 
            return False
        else:
            return True

food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)

def create_spend_chart(categories):
    pass