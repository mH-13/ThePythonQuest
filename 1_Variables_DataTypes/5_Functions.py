# Functions in Python

# A function is a block of code which only runs when it is called. 
# You can pass data, known as parameters, into a function. 
# A function can return data as a result.

# Defining a function
def my_function():
  print("Hello from a function")

# Calling a function
my_function()

# Functions with parameters
def greet(name):
  print(f"Hello, {name}")

greet("Alice")

# Functions with return values
def add(a, b):
  return a + b

result = add(3, 4)
print(result)

# Default parameter values
def greet(name="Guest"):
  print(f"Hello, {name}")

greet()
greet("Bob")

# Keyword arguments
def describe_pet(animal_type, pet_name):
  print(f"I have a {animal_type} named {pet_name}")

describe_pet(animal_type="dog", pet_name="Rex")
describe_pet(pet_name="Whiskers", animal_type="cat")

# Arbitrary arguments (*args)
def fruits(*args):
  for fruit in args:
    print(fruit)

fruits("apple", "banana", "cherry")

# Arbitrary keyword arguments (**kwargs)
def person_info(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}: {value}")

person_info(name="Alice", age=30, city="New York")

# Lambda functions (anonymous functions)
square = lambda x: x * x
print(square(5))

# Higher-order functions (functions that take other functions as arguments)
def apply_function(func, value):
  return func(value)

print(apply_function(square, 6))

# Nested functions
def outer_function(text):
  def inner_function():
    print(text)
  inner_function()

outer_function("Hello from nested function")

# Closures
def make_multiplier(x):
  def multiplier(n):
    return x * n
  return multiplier

times3 = make_multiplier(3)
print(times3(10))

# Decorators (functions that modify other functions)
def my_decorator(func):
  def wrapper():
    print("Something is happening before the function is called.")
    func()
    print("Something is happening after the function is called.")
  return wrapper

@my_decorator
def say_hello():
  print("Hello!")

say_hello()

# Recursion (a function that calls itself)
def factorial(n):
  if n == 1:
    return 1
  else:
    return n * factorial(n-1)

print(factorial(5))








# Functions in Python

# A function is a block of reusable code that performs a specific task.
# Functions help in organizing code, making it modular and easier to maintain.

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





