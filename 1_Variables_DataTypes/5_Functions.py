# Functions in Python
# A function is a block of code that performs a specific task. It can take inputs, process them, and return an output.

# Defining a Function
def my_function():
  print("Hello from a function") 

# Use Case: Basic function to print a greeting message
my_function()  # Output: Hello from a function

# Function with Parameters
def greet(name):
  print(f"Hello, {name}")

greet("Alice")  # Output: Hello, Alice


def bonjour(name):
  print(f"Bonjour, {name }")

for _ in range(5): bonjour(input("Enter your name: ")) 
# Output: Bonjour, {name} (5 times)

# Function with Return Value
def add(a, b):
  """This function takes two numbers and returns their sum."""
  return a + b

result = add(3, 4)
print(result)  # Output: 7

# Default Parameter Values
def greet(name="Guest"):
  """This function greets a user, with a default name if none is provided."""
  print(f"Hello, {name}")

# Use Case: Greeting with optional name
greet()  # Output: Hello, Guest
greet("Bob")  # Output: Hello, Bob

# Keyword Arguments
def describe_pet(animal_type, pet_name):
  """This function describes a pet using keyword arguments."""
  print(f"I have a {animal_type} named {pet_name}")

# Use Case: Describing pets with keyword arguments
describe_pet(animal_type="dog", pet_name="Rex")
describe_pet(pet_name="Whiskers", animal_type="cat")

# Arbitrary Arguments (*args)
# The *args parameter allows a function to accept an arbitrary number of positional arguments.
# The arguments are stored in a tuple.
# You can use any name for the *args parameter, but args is commonly used for readability.
# The * symbol is used to unpack the arguments when calling the function.
# The arguments can be accessed by iterating over the tuple or using indexing.
# The *args parameter must be placed at the end of the parameter list.
# You can combine *args with other parameters in the function definition.

def fruits(*args):
  """This function takes an arbitrary number of arguments and prints them."""
  for fruit in args:
    print(fruit)

# Use Case: Listing fruits
fruits("apple", "banana", "cherry")

# Arbitrary Keyword Arguments (**kwargs)
# The **kwargs parameter allows a function to accept an arbitrary number of keyword arguments.
# The arguments are stored in a dictionary.
# You can use any name for the **kwargs parameter, but kwargs is commonly used for readability.
# The ** symbol is used to unpack the keyword arguments when calling the function.
# The arguments can be accessed by iterating over the dictionary or using key-value pairs.
# The **kwargs parameter must be placed at the end of the parameter list.
# You can combine **kwargs with other parameters in the function definition.
# The keys in the dictionary are the parameter names, and the values are the argument values.
# The **kwargs parameter is useful when you want to accept multiple keyword arguments of varying types.
# You can use any name for the keys in the dictionary when calling the function.
# The **kwargs parameter is often used in functions that need to accept optional or extra arguments.
# The **kwargs parameter is commonly used in decorators and functions that need to pass arguments to other functions.
# The **kwargs parameter is useful when you want to pass a dictionary of arguments to another function and a function that accepts keyword arguments.

def person_info(**kwargs):
  """This function takes arbitrary keyword arguments and prints them."""
  for key, value in kwargs.items():
    print(f"{key}: {value}")

# Use Case: Displaying person information
person_info(name="Alice", age=30, city="New York")

# Lambda Functions (Anonymous Functions)
square = lambda x: x * x

# Use Case: Calculating the square of a number
print(square(5))  # Output: 25

# Higher-order Functions
def apply_function(func, value):
  """This function takes another function and a value, and applies the function to the value."""
  return func(value)

# Use Case: Applying a function to a value
print(apply_function(square, 6))  # Output: 36

# Nested Functions
def outer_function(text):
  """This function contains a nested function."""
  def inner_function():
    print(text)
  inner_function()

# Use Case: Using nested functions
outer_function("Hello from nested function")

# Closures
def make_multiplier(x):
  """This function returns a closure that multiplies its input by x."""
  def multiplier(n):
    return x * n
  return multiplier

# Use Case: Creating a multiplier function
times3 = make_multiplier(3)
print(times3(10))  # Output: 30

# Decorators
def my_decorator(func):
  """This is a decorator function that modifies another function."""
  def wrapper():
    print("Something is happening before the function is called.")
    func()
    print("Something is happening after the function is called.")
  return wrapper

@my_decorator
def say_hello():
  """This function prints a hello message."""
  print("Hello!")

# Use Case: Using a decorator to modify a function
say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

# Recursion
def factorial(n):
  """This function calculates the factorial of a number using recursion."""
  if n == 1:
    return 1
  else:
    return n * factorial(n-1)

# Use Case: Calculating factorial of a number
print(factorial(5))  # Output: 120
# A function is a block of code which only runs when it is called. 
# You can pass data, known as parameters, into a function. 
# A function can return data as a result.




#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
# Functions in Python


# Example 1: Basic Function
def greet():
    """This function greets the user."""  # Docstring: Describes the function
    print("Hello, welcome to Python!")

# Use Case: Greeting users in an application
greet()  # Calling the function

# Example 2: Function with Parameters
def greet_user(name):
    """Greets a specific user by their name."""
    print(f"Hello, {name}! Welcome to Python.")

# Use Case: Personalizing greetings in a user interface
greet_user("Alice")  # Hello, Alice! Welcome to Python.
greet_user("Bob")    # Hello, Bob! Welcome to Python.

# Example 3: Function with Return Value
def add(a, b):
    """Adds two numbers and returns the result."""
    return a + b

# Use Case: Calculating the sum of two numbers in a calculator app
result = add(5, 3)
print("Sum:", result)  # Sum: 8

# Example 4: Default Arguments
def greet_user_with_default(name="Guest"):
    """Greets a user with a default name if not provided."""
    print(f"Hello, {name}! Welcome to Python.")

# Use Case: Handling cases where user input is optional
greet_user_with_default()        # Hello, Guest! Welcome to Python.
greet_user_with_default("Alice") # Hello, Alice! Welcome to Python.

# Example 5: Keyword Arguments
def describe_person(name, age, city):
    """Describes a person using keyword arguments."""
    print(f"{name} is {age} years old and lives in {city}.")

# Use Case: Passing arguments in any order for clarity
describe_person(name="Alice", age=25, city="New York")
describe_person(city="London", name="Bob", age=30)

# Example 6: Variable-Length Arguments (*args)
def calculate_sum(*numbers):
    """Calculates the sum of any number of arguments."""
    total = 0
    for num in numbers:
        total += num
    return total

# Use Case: Summing a dynamic list of numbers in a calculator app
print("Sum of 1, 2, 3:", calculate_sum(1, 2, 3))  # Sum of 1, 2, 3: 6
print("Sum of 4, 5, 6, 7:", calculate_sum(4, 5, 6, 7))  # Sum of 4, 5, 6, 7: 22

# Example 7: Variable-Length Keyword Arguments (**kwargs)
def describe_car(**details):
    """Prints details about a car using keyword arguments."""
    for key, value in details.items():
        print(f"{key}: {value}")

# Use Case: Storing and displaying dynamic car details
describe_car(make="Toyota", model="Corolla", year=2020)
# Output:
# make: Toyota
# model: Corolla
# year: 2020

# Example 8: Lambda Functions (Anonymous Functions)
# Lambda functions are small, one-line functions without a name.
square = lambda x: x ** 2

# Use Case: Quick calculations or operations in data processing
print("Square of 5:", square(5))  # Square of 5: 25

# Example 9: Recursive Function
def factorial(n):
    """Calculates the factorial of a number using recursion."""
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Use Case: Calculating factorial in mathematical applications
print("Factorial of 5:", factorial(5))  # Factorial of 5: 120

