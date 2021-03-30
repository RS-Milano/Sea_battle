class Clients:
    def __init__(self, name = None, account_balance = None):
        if name is None:
            name = input("Enter customer name: ")
        self.name = name
        if account_balance is None:
            while True:
                account_balance = input("Enter account balance: ")
                if len(set(account_balance).union(set("0123456789."))) == 11 and account_balance.find(".") == account_balance.rfind("."):
                    account_balance = float(account_balance)
                    break
                print("Incorrect input, expected integer or float")
        self.account_balance = account_balance

    def get_name(self):
        return self.name

    def get_account_balance(self):
        return self.account_balance

    def top_up_account(self, income):
        if isinstance(income, (int, float)):
            self.account_balance += income
        else:
            return "Expected integer or float"

    def write_offs(self, outcome):
        if isinstance(outcome, (int, float)):
            if self.account_balance >= outcome:
                self.account_balance -= outcome
            else:
                return "Account has insufficient funds"
        else:
            return "Expected integer or float"

user = Clients()
print(user.get_account_balance())
user.top_up_account(230.9)
user.write_offs(175.1)
print(user.get_account_balance())