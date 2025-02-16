"""This module provides an overview of Python operators with use cases and examples.

Operators are special symbols in Python that carry out arithmetic or logical computation. The value that the operator operates on is called the operand.

1. Arithmetic Operators
2. Comparison (Relational) Operators
3. Logical Operators
4. Bitwise Operators
5. Assignment Operators
6. Identity Operators
7. Membership Operators
"""

# 1. Arithmetic Operators
# These operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.

a = 10
b = 5

print("Addition:", a + b)        # Output: 15
print("Subtraction:", a - b)     # Output: 5
print("Multiplication:", a * b)  # Output: 50
print("Division:", a / b)        # Output: 2.0
print("Modulus:", a % b)         # Output: 0 (remainder of division)
print("Exponentiation:", a ** b) # Output: 100000 (10^5)
print("Floor Division:", a // b) # Output: 2 (rounds down to the nearest integer)

# 2. Comparison (Relational) Operators
# These operators compare the values on either side of them and decide the relation among them.

print("Equal:", a == b)          # Output: False
print("Not Equal:", a != b)      # Output: True
print("Greater than:", a > b)    # Output: True
print("Less than:", a < b)       # Output: False
print("Greater than or equal to:", a >= b) # Output: True
print("Less than or equal to:", a <= b)    # Output: False

# 3. Logical Operators
# These operators are used to combine conditional statements.

x = True
y = False

print("AND:", x and y)           # Output: False
print("OR:", x or y)             # Output: True
print("NOT:", not x)             # Output: False

# 4. Bitwise Operators
# These operators are used to perform bit-level operations.
# 
c = 6  # 110 in binary
d = 2  # 010 in binary

print("Bitwise AND:", c & d)     # Output: 2 (010) 
print("Bitwise OR:", c | d)      # Output: 6 (110)
print("Bitwise XOR:", c ^ d)     # Output: 4 (100) 
print("Bitwise NOT:", ~c)        # Output: -7
print("Bitwise LEFT SHIFT:", c << 1) # Output: 12 (1100)
print("Bitwise RIGHT SHIFT:", c >> 1) # Output: 3 (011)

# Bitwise operations are used to manipulate individual bits of data. They are often used in low-level programming, such as systems programming, device drivers, and network protocol implementations.

# Use cases:
# 1. Setting, clearing, and toggling specific bits in a byte or word.
# 2. Performing fast arithmetic operations.
# 3. Encoding and decoding data.
# 4. Implementing bit masks for permissions and flags.

# How they work:
# - Bitwise AND (&): Sets each bit to 1 if both bits are 1.
# - Bitwise OR (|): Sets each bit to 1 if one of two bits is 1.
# - Bitwise XOR (^): Sets each bit to 1 if only one of two bits is 1.
# - Bitwise NOT (~): Inverts all the bits.
# - Bitwise LEFT SHIFT (<<): Shifts bits to the left, filling with zeros.
# - Bitwise RIGHT SHIFT (>>): Shifts bits to the right, filling with the sign bit (for signed numbers).

# Example:
# Let's say we have two 8-bit numbers: 12 (00001100) and 5 (00000101)

# Bitwise AND
result = 12 & 5  # 00000100 (4)
print("12 & 5:", result)

# Bitwise OR
result = 12 | 5  # 00001101 (13)
print("12 | 5:", result)

# Bitwise XOR
result = 12 ^ 5  # 00001001 (9)
print("12 ^ 5:", result)

# Bitwise NOT
result = ~12  # 11110011 (-13 in two's complement)
print("~12:", result)

# Bitwise LEFT SHIFT
result = 12 << 2  # 00110000 (48)
print("12 << 2:", result)

# Bitwise RIGHT SHIFT
result = 12 >> 2  # 00000011 (3)
print("12 >> 2:", result)


# 5. Assignment Operators
# These operators are used to assign values to variables.ma

e = 5
e += 3  # e = e + 3
print("Add and assign:", e)      # Output: 8

e -= 2  # e = e - 2
print("Subtract and assign:", e) # Output: 6

e *= 2  # e = e * 2
print("Multiply and assign:", e) # Output: 12

e /= 3  # e = e / 3
print("Divide and assign:", e)   # Output: 4.0

e %= 3  # e = e % 3
print("Modulus and assign:", e)  # Output: 1.0

e **= 2  # e = e ** 2
print("Exponent and assign:", e) # Output: 1.0

e //= 2  # e = e // 2
print("Floor divide and assign:", e) # Output: 0.0

# 6. Identity Operators
# These operators are used to compare the memory locations of two objects.

f = [1, 2, 3]
g = [1, 2, 3]
h = f

print("Is:", f is h)             # Output: True
print("Is not:", f is not g)     # Output: True

# 7. Membership Operators
# These operators are used to test if a sequence is presented in an object.

print("In:", 1 in f)             # Output: True
print("Not in:", 4 not in f)     # Output: True







# Operators in Python

# 1. Arithmetic Operators
a = 10
b = 3

print("Addition:", a + b)       # 13
print("Subtraction:", a - b)    # 7
print("Multiplication:", a * b) # 30
print("Division:", a / b)       # 3.333...
print("Floor Division:", a // b) # 3 (rounds down to the nearest integer)
print("Modulus:", a % b)        # 1 (remainder of division)
print("Exponent:", a ** b)      # 1000 (10^3)

# 2. Comparison Operators
print("Equal to:", a == b)      # False
print("Not equal to:", a != b)  # True
print("Greater than:", a > b)   # True
print("Less than:", a < b)      # False
print("Greater than or equal to:", a >= b)  # True
print("Less than or equal to:", a <= b)     # False

# 3. Logical Operators
x = True
y = False

print("AND:", x and y)  # False (both must be True)
print("OR:", x or y)    # True (at least one must be True)
print("NOT:", not x)    # False (inverts the value)

# 4. Assignment Operators
c = 5
c += 2  # Equivalent to c = c + 2
print("c += 2:", c)  # 7

c -= 1  # Equivalent to c = c - 1
print("c -= 1:", c)  # 6

# 5. Membership Operators
fruits = ["apple", "banana", "cherry"]
print("Is 'banana' in fruits?", "banana" in fruits)  # True
print("Is 'mango' not in fruits?", "mango" not in fruits)  # True

# 6. Identity Operators
x = 10
y = 10
print("Is x the same as y?", x is y)  # True (same value and memory location)
print("Is x not the same as y?", x is not y)  # False