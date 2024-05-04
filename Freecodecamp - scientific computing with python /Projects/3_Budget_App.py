# Class representing a category of expenses.
# Classe che rappresenta una categoria di spese.

class Category:
    def __init__(self,category):
        # Constructor method initializing the category name and ledger.
        # Metodo costruttore che inizializza il nome della categoria e il registro.
        self.category=category
        self.ledger=[]

    def __str__(self):
        # Method returning a string representation of the category, including a title, entries, and total balance.
        # Metodo che restituisce una rappresentazione in stringa della categoria, incluso un titolo, voci e saldo totale.
        title = f'{self.category.center(30, "*")}\n'
        total= f'Total: {self.get_balance()}'
        entries=''
        for entry in self.ledger:
            des= entry["description"][:23].ljust(23)
            amt= f'{str("{:.2f}".format(float(entry["amount"]), 2)).rjust(7)}'
            entries+= f'{des}{amt}\n'
        return title+entries+total

    def deposit (self,amount,description=''):
        # Method for depositing funds into the category ledger.
        # Metodo per depositare fondi nel registro della categoria
        positive_amount=abs(amount)
        self.ledger.append({"amount": positive_amount, "description": description})

    def withdraw (self,amount,description=''):
        # Method for withdrawing funds from the category ledger.
        # Metodo per prelevare fondi dal registro della categoria.
        if self.check_funds(amount):
            negative_amount=abs(amount)*-1
            self.ledger.append({"amount": negative_amount, "description": description})
            return True
        else: 
            return False

    def get_balance(self):
        # Method for calculating the current balance of the category ledger.
        # Metodo per calcolare il saldo attuale del registro della categoria.
        current_balance=0
        for entry in self.ledger:
            current_balance += entry["amount"]
        return current_balance
    
    def get_balance_withdraw(self):
        # Method for calculating the total amount withdrawn from the category ledger.
        # Metodo per calcolare l'importo totale prelevato dal registro della categoria.
        withdraw_balance=0
        for entry in self.ledger:
            if entry["amount"] < 0:
                withdraw_balance += entry["amount"]
        return withdraw_balance
    
    def transfer(self,amount,category):
        # Method for transferring funds between categories.
        # Metodo per trasferire fondi tra categorie.
        if self.check_funds(amount):
            self.withdraw(amount,f'Transfer to {category.category}')
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        else:
            return False
        
    def check_funds(self,amount):
        # Method for checking if there are enough funds in the category ledger for a given withdrawal amount.
        # Metodo per controllare se ci sono abbastanza fondi nel registro della categoria per un determinato importo di prelievo.
        if amount > self.get_balance(): 
            return False
        else:
            return True

# Function for creating a bar chart representing the percentage spent by each category.
# Funzione per creare un grafico a barre che rappresenta la percentuale spesa da ogni categoria.   
def create_spend_chart(categories):
    # Create a string variable to represent the title of the spend chart.
    # Crea una variabile stringa per rappresentare il titolo del grafico di spesa per categoria.
    chart = "Percentage spent by category\n"
    
    # Calculate the maximum length of category names for formatting purposes.
    # Calcolare la lunghezza massima dei nomi delle categorie per scopi di formattazione.
    len_categories= []
    for category in categories:
        len_categories.append(len(str(category)))
    max_len = max(len_categories)

    # Calculate the percentage spent in each category.
    # Calcolare la percentuale spesa in ogni categoria.
    total_spend = sum(category.get_balance_withdraw() for category in categories)
    percentage_spend = [(category.get_balance_withdraw()/total_spend)*100 for category in categories]

    # Create the bar chart.
    # Creare il grafico a barre.
    for percentage in range(100,-1,-10): 
        chart+= f'{str(percentage).rjust(3)}| '
        for category_percentage in percentage_spend: 
            if int(category_percentage) >= percentage:
                chart+="o  "
            else:
                chart+="   "
        chart+= '\n'
    
    # Create the bottom line of the chart.
    # Creare la linea inferiore del grafico.
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Insert category labels below the chart.
    # Inserire le etichette delle categorie sotto il grafico.
    max_category_length = max(len(str(category.category)) for category in categories)
    for i in range(max_category_length):
        chart += "     "
        for category in categories:
            if i < len(str(category.category)):
                chart += str(category.category)[i] + "  "
            else:
                chart += "   "
        if i < max_len-1:
            chart += "\n"
    return chart

# Create instances of categories and perform transactions.
# Creare istanze di categorie e eseguire transazioni.
food = Category("Food")
entertainment= Category("Entertainment")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)

# Print category ledger and spend chart.
# Stampare il registro delle categorie e il grafico delle spese.
print(food)
categories = [food,clothing,entertainment]
print(create_spend_chart(categories))