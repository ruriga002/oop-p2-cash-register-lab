#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Default discount is 0 if not provided by user
        self.discount = 0

        # Running total of all items in cart
        self.total = 0

        # List of items in cart
        self.items = []

        # List of previous transactions
        self.previous_transactions = []

        # Default discount
        self.discount = 0

        # Validate and assign discount
        self.set_discount(discount)

    def set_discount(self, discount):
        # Ensure discount is an integer
        if isinstance(discount, int) and 0 <= discount <= 100:
            self.discount = discount
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity):
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

        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last_transaction = self.previous_transactions.pop()

        self.total -= (
            last_transaction["price"] *
            last_transaction["quantity"]
        )

        self.items.pop()