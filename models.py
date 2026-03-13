# The four classes are Menu, Food, Transaction, and Customer
# The specifics for the models can be read in bytebites_design.md


class Food:
    def __init__(self, name, price, category, quantity, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.quantity = quantity
        self.popularity_rating = popularity_rating

    def get_quantity(self):
        return self.quantity

    def add_quantity(self, amount):
        self.quantity += amount


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, food):
        self.items.append(food)

    def get_all_items(self):
        return self.items

    def filter_by_category(self, category):
        # Returns a list of Food items whose category matches the given category string
        return [item for item in self.items if item.category == category]


class Transaction:
    def __init__(self, items):
        self.items = items
        self.total_cost = self.compute_total()

    def compute_total(self):
        # Sums the price of all Food items in self.items and returns the total as a float
        return sum(item.price for item in self.items)


class Customer:
    def __init__(self, name):
        self.name = name
        self.transactions = []

    def login(self):
        return True

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def purchase_history(self):
        return self.transactions
