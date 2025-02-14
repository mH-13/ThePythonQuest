# loops.py

# For Loop
# A for loop is used for iterating over a sequence (list, tuple, dictionary, set, or string).

# Example: Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)

# Example: Iterating over a string
for char in "banana":
  print(char)

# Example: Iterating over a range of numbers
for i in range(5):
  print(i)

# Example: Using range with start and end
for i in range(2, 6):
  print(i)

# Example: Using range with start, end, and step
for i in range(2, 10, 2):
  print(i)

# While Loop
# A while loop will continue to execute a block of code as long as a condition is true.

# Example: Basic while loop
count = 0
while count < 5:
  print(count)
  count += 1

# Example: Using break to exit a loop
count = 0
while count < 5:
  if count == 3:
    break
  print(count)
  count += 1

# Example: Using continue to skip an iteration
count = 0
while count < 5:
  count += 1
  if count == 3:
    continue
  print(count)

# Nested Loops
# You can use one or more loops inside another loop.

# Example: Nested for loop
for i in range(3):
  for j in range(2):
    print(f"i: {i}, j: {j}")

# Example: Nested while loop
i = 0
while i < 3:
  j = 0
  while j < 2:
    print(f"i: {i}, j: {j}")
    j += 1
  i += 1

# One-liner for loop
# You can use a for loop in a single line for simple operations.

# Example: One-liner for loop to create a list of squares
squares = [x**2 for x in range(10)]
print(squares)

# Example: One-liner for loop with condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)

# One-liner while loop
# While loops are generally not used in one-liners, but simple cases can be written.

# Example: One-liner while loop to print numbers
count = 0
while count < 5: print(count); count += 1


# For Loop
for i in range(5):
    print(i)  # 0 1 2 3 4

# While Loop
count = 0
while count < 3:
    print(count)
    count += 1