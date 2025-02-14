# Integer variable
"""
This module demonstrates the use of various variable types in Python, including integers, floats, strings, booleans, lists, tuples, dictionaries, sets, and NoneType. It also includes examples of how to declare these variables and check their types.

Variables and Data Types:
- Integer variable: `integer_var` (e.g., 42)
- Float variable: `float_var` (e.g., 3.14)
- String variable: `string_var` (e.g., "Hello, World!")
- Boolean variable: `boolean_var` (e.g., True)
- List variable: `list_var` (e.g., [1, 2, 3, 4, 5])
- Tuple variable: `tuple_var` (e.g., (1, 2, 3, 4, 5))
- Dictionary variable: `dict_var` (e.g., {"name": "Alice", "age": 30, "city": "Wonderland"})
- Set variable: `set_var` (e.g., {1, 2, 3, 4, 5})
- NoneType variable: `none_var` (e.g., None)

Examples:
- String: `name = "Alice"`
- Integer: `age = 25`
- Float: `height = 5.6`
- Boolean: `is_student = True`

Usage:
- To declare a variable, simply assign a value to a variable name using the `=` operator.
- To check the type of a variable, use the `type()` function.

Example:

"""
integer_var = 42

# Float variable
float_var = 3.14

# String variable
string_var = "Hello, World!"

# Boolean variable
boolean_var = True

# List variable
list_var = [1, 2, 3, 4, 5]

# Tuple variable
tuple_var = (1, 2, 3, 4, 5)

# Dictionary variable
dict_var = {
  "name": "Alice",
  "age": 30,
  "city": "Wonderland"
}

# Set variable
set_var = {1, 2, 3, 4, 5}

# NoneType variable
none_var = None


# Variables and Data Types
name = "Alice"          # String
age = 25                # Integer
height = 5.6            # Float
is_student = True       # Boolean

print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>




# Variables and Data Types in Python

# Variables are used to store data in memory.
# Python is dynamically typed, so you don't need to declare the type explicitly.

# Example 1: Basic Variables
name = "Alice"  # String
age = 25        # Integer
height = 5.6    # Float
is_student = True  # Boolean

# Printing variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Example 2: Type Checking
print("Type of 'name':", type(name))       # <class 'str'>
print("Type of 'age':", type(age))         # <class 'int'>
print("Type of 'height':", type(height))   # <class 'float'>
print("Type of 'is_student':", type(is_student))  # <class 'bool'>

# Example 3: Reassigning Variables
age = 26  # Reassigning the value of 'age'
print("Updated Age:", age)

# Example 4: Multiple Assignment
a, b, c = 1, 2.5, "Hello"
print("a:", a, "b:", b, "c:", c)

# Example 5: Constants (Convention: Use uppercase for constants)
PI = 3.14159
print("Value of PI:", PI)















# Data Types in Python

# Python has several built-in data types:
# 1. Numeric: int, float, complex
# 2. Sequence: str, list, tuple
# 3. Boolean: bool
# 4. Set: set
# 5. Mapping: dict

# Example 1: Numeric Types
integer_num = 10          # int
float_num = 10.5          # float
complex_num = 3 + 4j      # complex

print("Integer:", integer_num)
print("Float:", float_num)
print("Complex:", complex_num)

# Example 2: Sequence Types
string = "Hello, Python!"  # str
list_data = [1, 2, 3, 4]   # list
tuple_data = (1, 2, 3, 4)   # tuple

print("String:", string)
print("List:", list_data)
print("Tuple:", tuple_data)

# Example 3: Boolean Type
is_valid = True  # bool
print("Boolean:", is_valid)

# Example 4: Set Type
set_data = {1, 2, 3, 4}  # set (unordered, unique elements)
print("Set:", set_data)

# Example 5: Mapping Type
dictionary = {"name": "Alice", "age": 25}  # dict (key-value pairs)
print("Dictionary:", dictionary)