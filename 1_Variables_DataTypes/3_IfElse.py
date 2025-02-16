"""
If-Else Statements in Python

If-else statements are used to execute a block of code based on a condition. 
The condition is evaluated, and if it is true, the code inside the if block is executed. 
If the condition is false, the code inside the else block is executed.

Syntax:
if condition:
    # code to execute if condition is true
else:
    # code to execute if condition is false

One-liner If-Else:
Python allows the use of a one-liner if-else statement for simple conditions.

Syntax:
value_if_true if condition else value_if_false

Example:
result = "Even" if num % 2 == 0 else "Odd"
"""

# One-liner If-Else Example
num = 5
result = "Even" if num % 2 == 0 else "Odd"
print(result)
# Example 1: Simple If-Else
age = 18

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Example 2: If-Elif-Else
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Example 3: Nested If-Else
num = 10

if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Non-positive number")