#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Initialize discount to 0 by default
        self.discount = 0

        # Running total cost of all items in cart
        self.total = 0

        # List to store items added to cart
        self.items = []

        # Stores previous transactions for voiding
        self.previous_transactions = []

        # Validate and set the discount
        self.set_discount(discount)

    def set_discount(self, discount):
        """
        Validates the discount value.
        Discount must be an integer between 0 and 100.
        """
        if isinstance(discount, int) and 0 <= discount <= 100:
            self.discount = discount
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        """
        Adds an item to the cash register.

        Parameters:
        - item: item name
        - price: cost of one item
        - quantity: number of items (default is 1)
        """

        # Update total cost based on quantity
        self.total += price * quantity

        # Add item to items list for each quantity
        for _ in range(quantity):
            self.items.append(item)

        # Save transaction details for possible voiding later
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        """
        Applies a percentage discount to the total.
        Prints a message if no discount exists.
        """

        # If discount is 0, there is nothing to apply
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        # Calculate discount amount
        discount_amount = self.total * (self.discount / 100)

        # Subtract discount from total
        self.total -= discount_amount

        # Return updated total after discount
        return (
            f"After the discount, "
            f"the total comes to ${self.total:.2f}"
        )

    def void_last_transaction(self):
        """
        Removes the most recent transaction.
        Updates total and items list accordingly.
        """

        # Check if there are transactions to remove
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        # Remove the last transaction
        last_transaction = self.previous_transactions.pop()

        # Subtract the transaction amount from total
        self.total -= (
            last_transaction["price"] *
            last_transaction["quantity"]
        )

        # Remove the correct number of items
        for _ in range(last_transaction["quantity"]):
            self.items.pop()