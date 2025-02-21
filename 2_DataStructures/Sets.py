"""
Sets in Python

A set is an unordered collection of unique elements. Sets are mutable, meaning you can add or remove elements after the set has been created. Sets are commonly used for membership testing, removing duplicates from a sequence, and mathematical operations like union, intersection, difference, and symmetric difference.

Creating a Set:
- You can create a set using curly braces {} or the set() function.

Examples:
"""

# Creating a set with curly braces
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Creating a set using the set() function
numbers = set([1, 2, 3, 4, 5])
print(numbers)

"""
Adding and Removing Elements:
- Use the add() method to add an element to a set.
- Use the remove() method to remove an element. If  not found, it raises a KeyError.
- Use the discard() method also remove an element but If not found, it does nothing.
- Use the pop() method to remove and return an arbitrary element from the set.
- Use the clear() method to remove all elements from the set.

Examples:
"""

# Adding elements
fruits.add("orange")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}

# Removing elements
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry', 'orange'} ; KeyError 

# Discarding elements
fruits.discard("banana")  # No error 
print(fruits)  # Output: {'apple', 'cherry', 'orange'}

# Popping elements
popped_element = fruits.pop() 
print(popped_element)  # Output: 'apple' (or any other element)
print(fruits)  # Output: {'cherry', 'orange'}

# Clearing the set
fruits.clear()
print(fruits)  # Output: set()

"""
Set Operations:
- Union: Combines elements from both sets (use | operator or union() method).
- Intersection: Returns elements common to both sets (use & operator or intersection() method).
- Difference: Returns elements in the first set but not in the second (use - operator or difference() method).
- Symmetric Difference: Returns elements in either set, but not in both (use ^ operator or symmetric_difference() method).

Other Useful Methods:
- issubset(): Checks if one set is a subset of another.
- issuperset(): Checks if one set is a superset of another.
- isdisjoint(): Checks if two sets have no elements in common.

"""
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
# Subset
print(set_a.issubset(set_b))  # Output: False

# Superset
print(set_a.issuperset(set_b))  # Output: False

# Disjoint
print(set_a.isdisjoint(set_b))  # Output: False



# Use Case: Removing duplicates from a list
shopping_list = ["apple", "banana", "apple", "cherry"]
unique_items = set(shopping_list)
print("Unique Items:", unique_items) # {'apple', 'banana', 'cherry'}

# Use Case: Managing a collection of tags
tags = {"python", "programming", "tutorial"}
tags.add("coding")
tags.remove("tutorial")
print("Updated Tags:", tags) # {'python', 'programming', 'coding'}

# Example 3: Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
print("Union:", set1 | set2)  # {1, 2, 3, 4, 5}

# Intersection
print("Intersection:", set1 & set2)  # {3}

# Difference
print("Difference:", set1 - set2)  # {1, 2}

# Symmetric Difference
print("symmetric_difference_set", set1 ^ set2)  # {1, 2, 4, 5}

# Use Case: Finding common interests between users
user1_interests = {"reading", "music", "sports"}
user2_interests = {"music", "movies", "travel"}
common_interests = user1_interests & user2_interests
print("Common Interests:", common_interests)  # {'music'}