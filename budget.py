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
    display += total_text
    return display

  def __repr__(self):
    return self.__str__()
    
def create_spend_chart(categories):
  display = "Percentage spent by category\n"
  percent_list = [None] * (len(categories) * 2 + 1)
  categories_name = []
  amounts = []
  
  for category in categories:
    categories_name.append(category.name)
    amount_used = 0
    
    for i in category.ledger:
      if i["amount"] < 0 and not i["description"].startswith("Transfer"):
        amount_used += i["amount"]  
    amounts.append(amount_used)
    
  start = 1
  for amount in amounts:
    amount_uses = amount * 10 / sum(amounts)
    percent_list.insert(start, int(amount_uses))
    start += 3
  
  for i in range(10, -1, -1):
    value = str(10 * i) + "|" 
    value = f"{value:>4}"
    for j in percent_list:
      if j is not None:
        if j >= i:
          value += "o"
        else:
          value += " "
      else:
        value += " "
    display += value + "\n"
    
  display += " " * 4 + "-" * (len(categories) * 3 + 1) 

  for j in range(max([len(i) for i in categories_name])):
    name_text = "\n" + " " * 5
    for i in range(len(categories)):
      try:
        name_text += categories_name[i][j] + " " * 2
      except:
        name_text += " " * 3
        continue
    display += name_text
  
  return display
