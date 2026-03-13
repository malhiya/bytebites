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
        pass

    def add_quantity(self, amount):
        pass


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, food):
        pass

    def get_all_items(self):
        pass

    def filter_by_category(self, category):
        pass


class Transaction:
    def __init__(self, items):
        self.items = items
        self.total_cost = 0.0

    def compute_total(self):
        pass


class Customer:
    def __init__(self, name, transaction_id):
        self.name = name
        self.transaction_id = transaction_id

    def login(self):
        pass

    def purchase_history(self):
        pass
