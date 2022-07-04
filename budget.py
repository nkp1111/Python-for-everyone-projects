class Category:
  
  def __init__(self, name):
    self.name = name
    self.ledger = list()
    
  def deposit(self, amount, description=""):
    new_dict = {"amount":amount, "description":description}
    self.ledger.append(new_dict)
    
  def withdraw(self, amount, description=""):
    new_dict = {"amount":-amount, "description":description}
    balance = self.get_balance()
    if balance < amount:
      return False
    else:
      self.ledger.append(new_dict)
      return True

  def get_balance(self):
    balance = 0
    for i in range(len(self.ledger)):
      balance += self.ledger[i]["amount"]

    return balance

  def transfer(self, amount, budget_category):
    description = "Transfer from " + self.name
    new_dict = {"amount":amount, "description":description}
    description = f"Transfer to {budget_category.name}"
    new_dict1 = {"amount":-amount, "description":description}
    balance = self.get_balance()
    if balance < amount:
      return False
    else:
      self.ledger.append(new_dict1)
      budget_category.ledger.append(new_dict)
      return True

  def check_funds(self, amount):
    balance = self.get_balance()
    if balance < amount:
      return False
    else:
      return True

  def __str__(self):
    display = ""
    name  = f"{self.name}"
    display += name.center(30, "*") + "\n"
    total = 0
    for i in range(len(self.ledger)):
      amount = self.ledger[i]['amount']
      total += amount
      amount = f"{amount:.2f}"
      display += f"{self.ledger[i]['description'][:23]:<23}" + f"{amount:>7}" + "\n"
      amount = float(amount)
      
    total_text = "Total: " + str(total)
    display += total_text + "\n"
    return display
    
def create_spend_chart(categories):
  pass