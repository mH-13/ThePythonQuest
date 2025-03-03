"""
Dictionaries  in Python is an unordered collection of items. Each item is stored as a key-value pair. 
Dictionaries are mutable, meaning they can be changed after creation. They are also dynamic,  allowing for the addition and removal of key-value pairs.

Creating a Dictionary:
Dictionaries can be created using curly braces {} with key-value pairs separated by a colon, or by using the dict() function.  """
# using curly braces
my_dict = {
  'name': 'Alice',
  'age': 25,
  'city': 'New York'
}

# using the dict() function
my_dict = dict(name='Alice', age=25, city='New York')

"""Values in a dictionary can be accessed using their corresponding keys. You can use square brackets [] or the get() method to access values. """
# Accessing values
name = my_dict['name']  # Output: 'Alice'
age = my_dict.get('age')  # Output: 25

"""Adding and Updating Items: You can add new key-value pairs or update existing ones by assigning a value to key. """

# Adding a new key-value pair
my_dict['email'] = 'alice@example.com'

# Updating an existing key-value pair
my_dict['age'] = 26

""" Removing Items: Items can be removed using the del statement, pop() method, or popitem() method. """
# Removing items using the del statement or pop() method or popitem() method 
# del just removes the key-value pair, pop() returns the value of the removed key, and popitem() returns the last inserted key-value pair. Time complexity: O(1) for del and pop(), O(1) for popitem() in Python 3.7+. 


# del statement
del my_dict['city']

# pop() method
email = my_dict.pop('email')  # Output: 'alice@example.com'

# popitem() method (removes and returns the last inserted key-value pair)
last_item = my_dict.popitem()


"""You can iterate through a dictionary using a for loop. By default, the loop iterates through keys, but you can also iterate through key-value pairs using the items() method.  """


# Iterating through keys
for key in my_dict:
  print(key, my_dict[key])

# Iterating through key-value pairs
for key, value in my_dict.items():
  print(key, value)


"""Checking for Key Existence: You can check if a key exists in a dictionary using the in keyword or the get() method. """
# Checking for key existence
if 'name' in my_dict:
  print('Name:', my_dict['name']) # Output: 'Alice' (if 'name' exists) otherwise, KeyError
  
# Using the get() method
age = my_dict.get('age', 'N/A')  # Output: 26 (if 'age' exists), 'N/A' (otherwise)



""" Dictionary Methods: Python provides several useful methods for dictionaries.

- clear(): Removes all items from the dictionary.
- copy(): Returns a shallow copy of the dictionary.
- fromkeys(seq, value): Creates a new dictionary with keys from seq and values set to value.
- keys(): Returns a view object of the dictionary's keys.
- values(): Returns a view object of the dictionary's values.
- items(): Returns a view object of the dictionary's key-value pairs.
- update(other_dict): Updates the dictionary with key-value pairs from other_dict.
- pop(key, default): Removes the item with the specified key and returns its value. If the key is not found, it returns default.
- popitem(): Removes and returns the last inserted key-value pair.
- setdefault(key, default): Returns the value of the specified key. If the key does not exist, it inserts the key with the specified default value.
- get(key, default): Returns the value of the specified key. If the key is not found, it returns default.
"""
# Using dictionary methods
my_dict.clear()  # Clears the dictionary
new_dict = my_dict.copy()  # Creates a shallow copy
keys = my_dict.keys()  # Returns a view object of keys
values = my_dict.values()  # Returns a view object of values
items = my_dict.items()  # Returns a view object of key-value pairs

""" Use Cases:
1. Storing and accessing configuration settings.
2. Counting occurrences of items (e.g., word frequency in a text).
3. Representing structured data (e.g., JSON objects).
4. Caching/memoization to store previously computed results.
"""

# Example use case: Counting word frequency in a text
text = "hello world hello"
word_count = {}

for word in text.split(): # Split the text into words and iterate through them 
  word_count[word] = word_count.get(word, 0) + 1 # Increment the count for each word in the dictionary 

print(word_count)  # Output: {'hello': 2, 'world': 1}



# counting the frequency of a number in a list and print the maximum frequency number and k maximum frequency numbers

numbers = [1, 2, 3, 4, 1, 2, 5, 6, 7, 1]
number_count = {} # Create an empty dictionary to store the frequency of each number

for num in numbers: # Iterate through the list of numbers
    number_count[num] = number_count.get(num, 0) + 1
    #get method returns the value of the key if it exists in the dictionary, otherwise it returns the default value (0 in this case)
    #get(num, 0) + 1 is equivalent to number_count[num] = number_count[num] + 1 if num exists in the dictionary, otherwise number_count[num] = 0 + 1 = 1 
    
max_freq_num = max(number_count, key=number_count.get) # Find the number with the maximum frequency
#number_count.get is a function that returns the value of the key in the dictionary. 
#max function returns the key with the maximum value based on the number_count dictionary
#key parameter specifies a function that is used to extract the comparison key from each element in the iterable


print("Number with the maximum frequency:", max_freq_num) # Output: 1

#find the k maximum frequency numbers
k = 2
max_freq_nums = sorted(number_count, key=number_count.get, reverse=True)[:k] 
# Find the k numbers with the maximum frequency 
# sorted function sorts the numbers based on the frequency in descending order (reverse=True) and returns the first k numbers 
# [:k] is used to get the first k elements from the sorted list 

print(f"{k} numbers with the maximum frequency:", max_freq_nums) # Output: [1, 2] (if k=2) 


    


#Direc examples 
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

# Example 6: Removing Items from a Dictionary
del student["major"]  # Remove a key-value pair
email = user_profile.pop("email")  # Remove and return the value of a key
print("Updated Student:", student)
print("Updated User Profile:", user_profile)
print("Removed Email:", email)  
