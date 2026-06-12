#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Default discount is 0 if not provided by user
        self.discount = 0

        # Running total of all items in cart
        self.total = 0

        # Stores names of items added to cart
        self.items = []

        # Keeps history of all transactions for undo/void feature
        self.previous_transactions = []

        # Validate and assign discount if valid
        self.set_discount(discount)

    def add_item(self, item, price, quantity):
        # Update total price based on item price and quantity
        self.total += price * quantity

    # Track item in cart
    self.items.append(item)

    # Store transaction for possible rollback (void feature)
    self.previous_transactions.append({
        "item": item,
        "price": price,
        "quantity": quantity
    })
