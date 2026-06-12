# Object Oriented Programming (OOP) Part 2 – Cash Register Lab

## Overview

The **Cash Register Lab** is a Python-based Object-Oriented Programming (OOP) project that simulates the functionality of a digital cash register used in an e-commerce environment. This application demonstrates core OOP concepts including **classes, attributes, methods, encapsulation, validation, and transaction management**.

The project allows users to:

* Add items to a cart
* Track total purchase cost
* Apply percentage discounts
* Void previous transactions
* Store transaction history

This lab was completed as part of an Object-Oriented Programming curriculum to strengthen understanding of class-based design and state management in Python.

---

## Features

### Cash Register Functionality

✅ Add items to a shopping cart
✅ Calculate running totals automatically
✅ Apply percentage-based discounts
✅ Track previous transactions
✅ Void the most recent transaction
✅ Input validation for discounts
✅ Unit testing with `pytest`

---

## Technologies Used

* **Python 3**
* **Pytest** (for testing)
* **Git & GitHub**
* **VS Code**

---

## Project Structure

```bash
cash-register-lab/
│── .github/
│── lib/
│   ├── cash_register.py
│   └── testing/
│       ├── cash_register_test.py
│       └── conftest.py
│── .gitignore
│── README.md
│── pytest.ini
│── Pipfile
│── Pipfile.lock
```

---

## Class Design

### `CashRegister` Class

The application is built around a `CashRegister` class.

### Attributes

| Attribute               | Description                              |
| ----------------------- | ---------------------------------------- |
| `discount`              | Percentage discount applied to the total |
| `total`                 | Running total of all cart items          |
| `items`                 | List of items currently in cart          |
| `previous_transactions` | Stores transaction history for voiding   |

### Methods

#### `add_item(item, price, quantity)`

Adds an item to the register.

**Responsibilities:**

* Updates total cost
* Stores item in cart
* Saves transaction history

#### `apply_discount()`

Applies a percentage discount to the total purchase amount.

**Responsibilities:**

* Reduces total price
* Validates discount availability
* Handles missing transactions safely

#### `void_last_transaction()`

Removes the most recent transaction.

**Responsibilities:**

* Updates total correctly
* Removes item from cart
* Removes previous transaction history
* Displays error message if no transaction exists

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/oop-p2-cash-register-lab.git
```

### 2. Navigate Into the Project

```bash
cd oop-p2-cash-register-lab
```

### 3. Install Dependencies

```bash
npm install
```

or install Python dependencies using:

```bash
pipenv install
```

---

## Running the Application

Run the project using Python:

```bash
python3 lib/cash_register.py
```

---

## Running Tests

This project uses **Pytest** for automated testing.

Run tests with:

```bash
pytest
```

Successful tests confirm that:

* Items are added correctly
* Totals update accurately
* Discounts apply properly
* Transactions can be voided
* Invalid discounts are handled

---

## Example Usage

```python
register = CashRegister(20)

register.add_item("Shoes", 50, 2)
register.add_item("Hat", 20, 1)

register.apply_discount()

print(register.total)
```

---

## Screenshot of Completed Work

Add your screenshot inside an `images` folder and reference it below.

```md
![Cash Register Lab Screenshot](./images/cash-register-screenshot.png)
```

Example:

![Cash Register Lab Screenshot](./images/cash-register-screenshot.png)

---

## What I Learned

Through this lab, I gained experience with:

* Object-Oriented Programming in Python
* Class construction using `__init__`
* Managing object state
* Writing reusable methods
* Data validation
* Testing Python applications with `pytest`
* Using GitHub workflows for version control

---

## Future Improvements

Potential enhancements for this project include:

* GUI integration
* Persistent transaction storage
* Receipt generation
* Multiple discount support
* Tax calculations
* Inventory tracking

---

## Author

**Your Name**
GitHub: https://github.com/YOUR-USERNAME

---

## License

This project is for educational purposes as part of an Object-Oriented Programming course.
