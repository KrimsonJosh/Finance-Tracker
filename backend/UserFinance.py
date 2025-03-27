class UserFinance:
    def __init__(self, name: str):
        self.name = name
        self.income = 0
        self.expenses = {} # Key-value pairs of expensive-price.

    def add_income(self, value: float) -> None:
        self.income += value 
    def remove_income(self, value: float) -> None:
        self.income -= value 
        self.income = abs(self.income) # If self.income < than 0, make it 0.
    
    def add_expense(self, expense: str, cost: float) -> None:
        if cost < 0:
            cost = 0 # Error handling
        self.expenses[expense] = cost 
    def remove_expense(self, expense: str) -> None:
        if expense not in self.expenses:
            return 
        del self.expenses[expense] 
    
    def calculate_balance(self) -> float:
        total_expense = sum(cost for cost in self.expenses.values())
        return self.income - total_expense 
    
    def monthly_expenses(self) -> float:
        total_expense = sum(cost for cost in self.expenses.values())
        return (self.income - total_expense) / 12