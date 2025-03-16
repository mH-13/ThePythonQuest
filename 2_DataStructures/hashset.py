""" HashSet is a data structure that implements a set using a hash table. It provides fast insertion, deletion, and lookup operations. In Python, the built-in `set` type is implemented as a hash set.

Features:
- Unordered collection of unique elements.
- Fast membership testing.
- Supports set operations like union, intersection, difference, and symmetric difference. """

# Creating a HashSet
hash_set = set()

# Adding elements to the HashSet
hash_set.add(1)
hash_set.add(2)
hash_set.add(3)

# Trying to add a duplicate element (will have no effect)
hash_set.add(2)

# Empty set
my_set = set()

# Initialize with elements
fruits = {"apple", "banana", "cherry"}

# Removing elements from the HashSet
hash_set.remove(1)  # Raises KeyError if the element is not present
hash_set.discard(4)  # Does nothing if the element is not present
fruits.remove("banana")    # Raises KeyError if missing
fruits.discard("grape")    # No error if missing
popped = fruits.pop()      # Removes an arbitrary element

# Checking membership
print(2 in hash_set)  # Output: True
print(1 in hash_set)  # Output: False

# Set operations
another_set = {3, 4, 5}



# Union
union_set = hash_set.union(another_set)
print(union_set)  # Output: {2, 3, 4, 5}

# Intersection
intersection_set = hash_set.intersection(another_set)
print(intersection_set)  # Output: {3}

# Difference
difference_set = hash_set.difference(another_set)
print(difference_set)  # Output: {2}

# Symmetric Difference
symmetric_difference_set = hash_set.symmetric_difference(another_set)
print(symmetric_difference_set)  # Output: {2, 4, 5}

set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a | set_b)   # Union: {1, 2, 3, 4, 5}
print(set_a & set_b)   # Intersection: {3}
print(set_a - set_b)   # Difference: {1, 2}
print(set_a ^ set_b)   # Symmetric Difference: {1, 2, 4, 5}

#removing duplicate
numbers = [1, 2, 2, 3, 4, 4]
unique_numbers = list(set(numbers))   # [1, 2, 3, 4] (order not preserved)


#fast membership testing
valid_users = {"alice", "bob", "charlie"}
username = input("Enter username: ")
print("Valid user!" if username in valid_users else "Invalid user!")

# Iterating over a HashSet
for element in hash_set:
  print(element)

# Clearing the HashSet
hash_set.clear()
print(hash_set)  # Output: set()



"""
Usage Scenarios:

1. Removing Duplicates: HashSets are useful for removing duplicates from a list while preserving unique elements.

2. Membership Testing: HashSets provide O(1) average time complexity for membership testing, making them efficient for checking if an element exists in a collection.

3. Set Operations: HashSets support mathematical set operations like union, intersection, difference, and symmetric difference, which are useful in various algorithms and data processing tasks.

Documentation

Method      	    Description
add(element)	    Adds a single element to the set.
update(iter)	    Adds multiple elements from an iterable.
remove(element)	  Removes an element (raises KeyError if missing).
discard(element)	Removes an element (no error if missing).
pop()	            Removes and returns an arbitrary element.
clear()	          Removes all elements from the set.
Properties:

Unordered: No index-based access (use lists for ordered data).

Mutable: Can modify elements, but stored elements must be hashable (immutable).

Dynamic Sizing: Automatically resizes as elements are added/removed.

Syntax Tips:

Use {} for non-empty sets (e.g., {1, 2, 3}) and set() for empty sets.

Use set comprehensions: {x for x in iterable}.


"""

