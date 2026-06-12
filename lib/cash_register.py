#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Default discount is 0 if not provided by user
        self.discount = 0

        # Running total of all items in cart
        self.total = 0
        # List of items in cart
        self.items = []
        # List of previous transactions for voiding purposes
        self.previous_transactions = []

        # Validate and assign discount if valid
        self.set_discount(discount)

    def add_item(self, item, price, quantity):
      # Validate inputs
        self.total += price * quantity
        self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        self.total -= (self.discount / 100) * self.total
        self.previous_transactions.pop()
        self.items.pop()

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        last = self.previous_transactions.pop()
        self.total -= last["price"] * last["quantity"]

        if last["item"] in self.items:
            self.items.remove(last["item"])