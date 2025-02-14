"""
This module provides an overview of lists in Python, including their creation, manipulation, and common operations.

A list is a collection data type that is ordered and mutable. Lists are defined by enclosing elements in square brackets [].
"""

# Creating a list
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "two", 3.0, [4, 5]]

# Accessing elements
first_element = numbers[0]  # Access the first element
last_element = numbers[-1]  # Access the last element

# Slicing a list
sub_list = numbers[1:3]  # Get elements from index 1 to 2

# Modifying elements
numbers[0] = 10  # Change the first element to 10

# Adding elements
numbers.append(6)  # Add 6 to the end of the list
numbers.insert(1, 15)  # Insert 15 at index 1

# Removing elements
numbers.remove(15)  # Remove the first occurrence of 15
popped_element = numbers.pop()  # Remove and return the last element
del numbers[0]  # Delete the first element

# List operations
length = len(numbers)  # Get the number of elements in the list
concatenated_list = numbers + [7, 8, 9]  # Concatenate two lists
repeated_list = numbers * 2  # Repeat the list

# List comprehension
squares = [x**2 for x in range(10)]  # Create a list of squares

# Common list methods
numbers.extend([7, 8, 9])  # Extend the list by appending elements from another list
index_of_3 = numbers.index(3)  # Get the index of the first occurrence of 3
count_of_3 = numbers.count(3)  # Count the number of occurrences of 3
numbers.sort()  # Sort the list in ascending order
numbers.reverse()  # Reverse the elements of the list

# Iterating through a list
for number in numbers:
  print(number)

# Nested lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
first_sublist = nested_list[0]  # Access the first sublist
first_element_of_first_sublist = nested_list[0][0]  # Access the first element of the first sublist







# Lists in Python

# A list is a mutable, ordered collection of items. It can store elements of different data types.

# Example 1: Creating a List
fruits = ["apple", "banana", "cherry"]
print("Fruits List:", fruits)

# Use Case: Storing a list of items in a shopping cart
shopping_cart = ["bread", "milk", "eggs"]
print("Shopping Cart:", shopping_cart)

# Example 2: Accessing List Elements
print("First Fruit:", fruits[0])  # apple
print("Last Fruit:", fruits[-1])  # cherry

# Use Case: Displaying the first item in a to-do list
todo_list = ["Buy groceries", "Pay bills", "Call mom"]
print("First Task:", todo_list[0])  # Buy groceries

# Example 3: Modifying Lists
fruits[1] = "blueberry"  # Replace "banana" with "blueberry"
print("Updated Fruits List:", fruits)

# Use Case: Updating a list of tasks
todo_list[1] = "Pay electricity bill"
print("Updated To-Do List:", todo_list)

# Example 4: Adding Elements
fruits.append("orange")  # Add "orange" to the end
print("After Append:", fruits)

fruits.insert(1, "mango")  # Insert "mango" at index 1
print("After Insert:", fruits)

# Use Case: Adding new items to a shopping list
shopping_cart.append("butter")
shopping_cart.insert(1, "cheese")
print("Updated Shopping Cart:", shopping_cart)

# Example 5: Removing Elements
fruits.remove("cherry")  # Remove "cherry"
print("After Remove:", fruits)

popped_item = fruits.pop(1)  # Remove and return item at index 1
print("Popped Item:", popped_item)
print("After Pop:", fruits)

# Use Case: Removing completed tasks from a to-do list
todo_list.remove("Buy groceries")
print("Updated To-Do List:", todo_list)

# Example 6: List Slicing
print("First Two Fruits:", fruits[:2])  # ['apple', 'mango']
print("Last Two Fruits:", fruits[-2:])  # ['blueberry', 'orange']

# Use Case: Displaying a subset of items in a list
print("First Two Tasks:", todo_list[:2])

# Example 7: List Operations
numbers = [1, 2, 3]
numbers.extend([4, 5])  # Add multiple items
print("Extended List:", numbers)

# Use Case: Combining two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Combined List:", combined_list)

# Example 8: List Comprehension
squares = [x ** 2 for x in range(5)]
print("Squares:", squares)  # [0, 1, 4, 9, 16]

# Use Case: Generating a list of even numbers
evens = [x for x in range(10) if x % 2 == 0]
print("Even Numbers:", evens)  # [0, 2, 4, 6, 8]