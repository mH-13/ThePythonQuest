"""
This module demonstrates the basics of Object-Oriented Programming (OOP) in Python.

Classes:
  Person: A class representing a person with a name and age.
  Student: A subclass of Person representing a student with a student ID.

Usage:
  Create instances of Person and Student and demonstrate their methods.
"""

class Person:
  """
  A class to represent a person.

  Attributes:
    name (str): The name of the person.
    age (int): The age of the person.
  """

  def __init__(self, name, age):
    """
    The constructor for Person class.

    Parameters:
      name (str): The name of the person.
      age (int): The age of the person.
    """
    self.name = name
    self.age = age

  def greet(self):
    """
    Method to greet the person.

    Returns:
      str: A greeting message.
    """
    return f"Hello, my name is {self.name} and I am {self.age} years old."


class Student(Person):
  """
  A class to represent a student, which is a subclass of Person.

  Attributes:
    name (str): The name of the student.
    age (int): The age of the student.
    student_id (str): The student ID.
  """

  def __init__(self, name, age, student_id):
    """
    The constructor for Student class.

    Parameters:
      name (str): The name of the student.
      age (int): The age of the student.
      student_id (str): The student ID.
    """
    super().__init__(name, age)
    self.student_id = student_id

  def study(self):
    """
    Method to simulate the student studying.

    Returns:
      str: A message indicating the student is studying.
    """
    return f"{self.name} is studying."


# Example usage
if __name__ == "__main__":
  # Create a Person instance
  person = Person("Alice", 30)
  print(person.greet())

  # Create a Student instance
  student = Student("Bob", 20, "S12345")
  print(student.greet())
  print(student.study())
  
  
  # Classes and Objects in Python

# OOP is a programming paradigm that uses objects and classes to structure code.
# A class is a blueprint for creating objects, and an object is an instance of a class.

# Example 1: Defining a Class
class Dog:
    """A simple Dog class."""

    def __init__(self, name, age):
        """Constructor to initialize the object."""
        self.name = name  # Attribute
        self.age = age    # Attribute

    def bark(self):
        """Method to make the dog bark."""
        print(f"{self.name} says Woof!")

# Use Case: Modeling real-world entities (e.g., pets, users, products)
my_dog = Dog("Buddy", 3)  # Create an object
print("Dog Name:", my_dog.name)  # Access attribute
print("Dog Age:", my_dog.age)
my_dog.bark()  # Call method

# Example 2: Adding More Methods
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def celebrate_birthday(self):
        """Method to increment age."""
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")

# Use Case: Adding behavior to objects (e.g., aging, updating status)
my_dog = Dog("Buddy", 3)
my_dog.celebrate_birthday()  # Happy Birthday, Buddy! You are now 4 years old.

# Example 3: Class vs Object
# A class is a blueprint, and an object is an instance of that blueprint.
dog1 = Dog("Max", 2)
dog2 = Dog("Lucy", 5)

print("Dog 1 Name:", dog1.name)  # Max
print("Dog 2 Name:", dog2.name)  # Lucy

# Use Case: Creating multiple instances of the same class (e.g., users in a system)