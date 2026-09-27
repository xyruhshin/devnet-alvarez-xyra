"""
Module 2 — Lesson 4: Functions
Student: [Xyra Shannel B. Alvarez]
Date: [September 27, 2026]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Lists are used to store multiple values in one variable.
Loops are used to repeat a block of code multiple times.

============================================
KEY VOCABULARY
============================================
- Function: reusable block of code that performs a specific task
- Parameter: value or variable that a function receives
- Argument: actual value given to a function
- Function call: sends a result back from the function
(add more as needed)

============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

def calculate_total(price, quantity):
    total = price * quantity
    return total

price = 50
quantity = 3

total = calculate_total(price, quantity)
print(f"Total: ₱{total}")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
Sometimes I forget to include the parameter when calling a function,
which caused an error. I learned to check what information the function
needs before calling it.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
