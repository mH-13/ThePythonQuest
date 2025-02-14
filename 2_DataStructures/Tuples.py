"""
Tuples in Python

A tuple is a collection of ordered, immutable elements. Tuples are similar to lists, but unlike lists, tuples cannot be changed after their creation. Tuples are defined by enclosing the elements in parentheses ().

Key Characteristics of Tuples:
- Ordered: The elements in a tuple have a defined order.
- Immutable: Once a tuple is created, its elements cannot be changed, added, or removed.
- Heterogeneous: Tuples can contain elements of different data types.
- Indexed: Elements in a tuple can be accessed using their index, starting from 0.

Creating Tuples:
- Empty tuple: `empty_tuple = ()`
- Single element tuple: `single_element_tuple = (element,)` (Note the comma)
- Multiple elements tuple: `multiple_elements_tuple = (element1, element2, element3)`

Accessing Tuple Elements:
- By index: `element = tuple[index]`
- Slicing: `sub_tuple = tuple[start:end]`

Tuple Operations:
- Concatenation: `new_tuple = tuple1 + tuple2`
- Repetition: `repeated_tuple = tuple * n`
- Membership: `element in tuple`

Tuple Methods:
- `count(value)`: Returns the number of times a specified value appears in the tuple.
- `index(value)`: Returns the index of the first occurrence of the specified value.

Examples:
"""

# Creating tuples
empty_tuple = ()
single_element_tuple = (42,)
multiple_elements_tuple = (1, 2, 3, 4, 5)

# Accessing elements
first_element = multiple_elements_tuple[0]
last_element = multiple_elements_tuple[-1]

# Slicing tuples
sub_tuple = multiple_elements_tuple[1:4]

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2

# Repetition
repeated_tuple = tuple1 * 3

# Membership
is_in_tuple = 2 in tuple1

# Tuple methods
count_of_2 = tuple1.count(2)
index_of_3 = tuple1.index(3)

# Example usage
print("Empty tuple:", empty_tuple)
print("Single element tuple:", single_element_tuple)
print("Multiple elements tuple:", multiple_elements_tuple)
print("First element:", first_element)
print("Last element:", last_element)
print("Sub tuple:", sub_tuple)
print("Concatenated tuple:", concatenated_tuple)
print("Repeated tuple:", repeated_tuple)
print("Is 2 in tuple1:", is_in_tuple)
print("Count of 2 in tuple1:", count_of_2)
print("Index of 3 in tuple1:", index_of_3)




# Tuples in Python

# A tuple is an immutable, ordered collection of items. It is similar to a list but cannot be modified.

# Example 1: Creating a Tuple
coordinates = (10, 20)
print("Coordinates:", coordinates)

# Use Case: Storing fixed data like geographic coordinates
location = (40.7128, -74.0060)  # Latitude and Longitude of New York
print("Location:", location)

# Example 2: Accessing Tuple Elements
print("Latitude:", location[0])  # 40.7128
print("Longitude:", location[1])  # -74.0060

# Use Case: Extracting data from a tuple
student = ("Alice", 25, "Computer Science")
name, age, major = student  # Unpacking
print(f"{name} is {age} years old and studies {major}.")

# Example 3: Immutable Nature
# coordinates[0] = 15  # This will raise an error (tuples are immutable)

# Use Case: Using tuples for constants
DAYS_OF_WEEK = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Days of Week:", DAYS_OF_WEEK)

# Example 4: Tuple Operations
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print("Combined Tuple:", combined_tuple)  # (1, 2, 3, 4, 5, 6)

# Use Case: Combining fixed data sets
months = ("January", "February", "March")
additional_months = ("April", "May")
all_months = months + additional_months
print("All Months:", all_months)