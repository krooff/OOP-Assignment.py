
#Task 1: class BudgetCategory

def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name  # Private attribute
        self.__allocated_budget = allocated_budget  # Private attribute
        self.__remaining_budget = allocated_budget  # Initialize remaining budget
# Task 2: Setter and Getter for category name
def get_category_name(self):
    return self.__category_name

    def set_category_name(self, category_name):
        self.__category_name = category_name

    def get_allocated_budget(self):
        return self.__allocated_budget

def set_allocated_budget(self, allocated_budget):
        if allocated_budget < 0:
            raise ValueError("Allocated budget must be a positive number.")
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget  # Reset remaining budget

# Task 3: Method to add an expense to the category
def add_expense(self, amount):
        if amount < 0:
            raise ValueError("Expense amount must be a positive number.")
        if amount > self.__remaining_budget:
            raise ValueError("Expense exceeds remaining budget.")
        self.__remaining_budget -= amount

    # Method to display the budget category details
def display_category_summary(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget:.2f}")
        print(f"Remaining Budget: ${self.__remaining_budget:.2f}")
