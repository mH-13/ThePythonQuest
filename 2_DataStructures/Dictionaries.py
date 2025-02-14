"""
Dictionaries in Python

A dictionary in Python is an unordered collection of items. Each item is stored as a key-value pair. 
Dictionaries are mutable, meaning they can be changed after creation. They are also dynamic, 
allowing for the addition and removal of key-value pairs.

Creating a Dictionary:
Dictionaries can be created using curly braces {} with key-value pairs separated by a colon, or by using the dict() function.

Example:
"""
# Creating a dictionary using curly braces
my_dict = {
  'name': 'Alice',
  'age': 25,
  'city': 'New York'
}

# Creating a dictionary using the dict() function
my_dict = dict(name='Alice', age=25, city='New York')

"""
Accessing Values:
Values in a dictionary can be accessed using their corresponding keys.

Example:
"""
# Accessing values
name = my_dict['name']  # Output: 'Alice'
age = my_dict.get('age')  # Output: 25

"""
Adding and Updating Items:
You can add new key-value pairs or update existing ones by assigning a value to a key.

Example:
"""
# Adding a new key-value pair
my_dict['email'] = 'alice@example.com'

# Updating an existing key-value pair
my_dict['age'] = 26

"""
Removing Items:
Items can be removed using the del statement, pop() method, or popitem() method.

Example:
"""
# Using del statement
del my_dict['city']

# Using pop() method
email = my_dict.pop('email')  # Output: 'alice@example.com'

# Using popitem() method (removes and returns the last inserted key-value pair)
last_item = my_dict.popitem()

"""
Iterating Through a Dictionary:
You can iterate through a dictionary using a for loop.

Example:
"""
# Iterating through keys
for key in my_dict:
  print(key, my_dict[key])

# Iterating through key-value pairs
for key, value in my_dict.items():
  print(key, value)

"""
Dictionary Methods:
Python provides several useful methods for dictionaries.

- clear(): Removes all items from the dictionary.
- copy(): Returns a shallow copy of the dictionary.
- fromkeys(seq, value): Creates a new dictionary with keys from seq and values set to value.
- keys(): Returns a view object of the dictionary's keys.
- values(): Returns a view object of the dictionary's values.
- items(): Returns a view object of the dictionary's key-value pairs.
- update(other_dict): Updates the dictionary with key-value pairs from other_dict.

Example:
"""
# Using dictionary methods
my_dict.clear()  # Clears the dictionary
new_dict = my_dict.copy()  # Creates a shallow copy
keys = my_dict.keys()  # Returns a view object of keys
values = my_dict.values()  # Returns a view object of values
items = my_dict.items()  # Returns a view object of key-value pairs

"""
Use Cases:
1. Storing and accessing configuration settings.
2. Counting occurrences of items (e.g., word frequency in a text).
3. Representing structured data (e.g., JSON objects).
4. Caching/memoization to store previously computed results.
"""

# Example use case: Counting word frequency in a text
text = "hello world hello"
word_count = {}
for word in text.split():
  word_count[word] = word_count.get(word, 0) + 1

print(word_count)  # Output: {'hello': 2, 'world': 1}



# Dictionaries in Python

# A dictionary is a mutable, unordered collection of key-value pairs. It is useful for storing and retrieving data efficiently.

# Example 1: Creating a Dictionary
student = {"name": "Alice", "age": 25, "major": "Computer Science"}
print("Student Dictionary:", student)

# Use Case: Storing user profiles
user_profile = {
    "username": "alice123",
    "email": "alice@example.com",
    "is_active": True
}
print("User Profile:", user_profile)

# Example 2: Accessing Dictionary Elements
print("Name:", student["name"])  # Alice
print("Age:", student.get("age"))  # 25

# Use Case: Retrieving user information
print("Username:", user_profile["username"])  # alice123

# Example 3: Modifying Dictionaries
student["age"] = 26  # Update age
student["year"] = 2023  # Add new key-value pair
print("Updated Student:", student)

# Use Case: Updating user profile
user_profile["email"] = "alice_new@example.com"
print("Updated User Profile:", user_profile)

# Example 4: Dictionary Methods
keys = student.keys()  # Get all keys
values = student.values()  # Get all values
items = student.items()  # Get key-value pairs

print("Keys:", keys)
print("Values:", values)
print("Items:", items)

# Use Case: Iterating over a dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# Example 5: Dictionary Comprehension
squares = {x: x ** 2 for x in range(5)}
print("Squares Dictionary:", squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Use Case: Creating a mapping of items to their prices
prices = {"apple": 1.0, "banana": 0.5, "cherry": 2.0}
discounted_prices = {item: price * 0.9 for item, price in prices.items()}
print("Discounted Prices:", discounted_prices)