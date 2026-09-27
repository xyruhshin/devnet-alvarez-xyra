"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Xyra Shannel B. Alvarez
Date: September 26, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]
The Control Flow (if / elif / else) allows you to make decisions based on certain conditions.
The if statement checks whether a code is true and output the code if it is, then for elif statement
it checks another condition when the if condition/statement is false. And for else statement, 
it runs when none of the previous conditions are true.

============================================
KEY VOCABULARY
============================================
- condition: a statement that checks whether something is true or false
- if / elif / else: are used to control which block of code runs based on a condition
- comparison operator: are operators that is used to compare values, such as ==, >, <, >=, or <=
- boolean expression: results in either True or False
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

age = int(input("Enter you age: "))

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

The error I've encountered is not putting a colon after the statement. 

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
