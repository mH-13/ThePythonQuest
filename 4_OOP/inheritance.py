from abc import ABC, abstractmethod

"""
Object-Oriented Programming (OOP) in Python

OOP is a programming paradigm that uses objects and classes to structure software in a way that is easy to manage and extend. The four main principles of OOP are:

1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

Below is an explanation and example code for each principle.
"""

# 1. Encapsulation
# Encapsulation is the bundling of data and methods that operate on that data within a single unit, or class.
# It restricts direct access to some of the object's components, which is a means of preventing accidental interference and misuse of the data.

class EncapsulationExample:
  def __init__(self, value):
    self.__hidden_value = value  # Private variable

  def get_value(self):
    return self.__hidden_value

  def set_value(self, value):
    self.__hidden_value = value

# Usage
encap = EncapsulationExample(10)
print(encap.get_value())  # Output: 10
encap.set_value(20)
print(encap.get_value())  # Output: 20

# 2. Inheritance
# Inheritance is a way to form new classes using classes that have already been defined. It helps to reuse code and establish a relationship between different classes.

class Animal:
  def speak(self):
    pass

class Dog(Animal):
  def speak(self):
    return "Woof!"

class Cat(Animal):
  def speak(self):
    return "Meow!"

# Usage
dog = Dog()
cat = Cat()
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!

# 3. Polymorphism
# Polymorphism allows methods to do different things based on the object it is acting upon, even if they share the same name.

def animal_sound(animal):
  print(animal.speak())

# Usage
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!

# 4. Abstraction
# Abstraction is the concept of hiding the complex implementation details and showing only the necessary features of an object.


class AbstractAnimal(ABC):
  @abstractmethod
  def speak(self):
    pass

class AbstractDog(AbstractAnimal):
  def speak(self):
    return "Woof!"

class AbstractCat(AbstractAnimal):
  def speak(self):
    return "Meow!"

# Usage
abstract_dog = AbstractDog()
abstract_cat = AbstractCat()
print(abstract_dog.speak())  # Output: Woof!
print(abstract_cat.speak())  # Output: Meow!



# Inheritance in Python

# Inheritance allows a class to inherit attributes and methods from another class.
# The class being inherited from is called the parent class, and the inheriting class is called the child class.

# Example 1: Basic Inheritance
class Animal:
    """Parent class representing an animal."""
    def __init__(self, name):
        self.name = name

    def speak(self):
        """Method to make the animal speak."""
        print(f"{self.name} makes a sound.")

class Dog(Animal):  # Dog inherits from Animal
    """Child class representing a dog."""
    def speak(self):
        """Override the speak method."""
        print(f"{self.name} says Woof!")

# Use Case: Extending functionality of existing classes (e.g., adding specific behavior)
my_dog = Dog("Buddy")
my_dog.speak()  # Buddy says Woof!

# Example 2: Multiple Inheritance
class Bird:
    """Parent class representing a bird."""
    def fly(self):
        print(f"{self.name} is flying.")

class Parrot(Animal, Bird):  # Inherits from both Animal and Bird
    """Child class representing a parrot."""
    def speak(self):
        print(f"{self.name} says Squawk!")

# Use Case: Combining features from multiple classes (e.g., a hybrid object)
my_parrot = Parrot("Polly")
my_parrot.speak()  # Polly says Squawk!
my_parrot.fly()    # Polly is flying.

# Example 3: super() Function
class Cat(Animal):
    """Child class representing a cat."""
    def __init__(self, name, color):
        super().__init__(name)  # Call the parent class constructor
        self.color = color

    def speak(self):
        print(f"{self.name} says Meow!")

# Use Case: Initializing parent class attributes in the child class
my_cat = Cat("Whiskers", "Black")
print("Cat Color:", my_cat.color)  # Black
my_cat.speak()  # Whiskers says Meow!



""" 
Use Cases for OOP
Modeling Real-World Entities:

Representing users, products, or animals in a system.

Example: A User class for a social media app.

Code Reusability:

Using inheritance to reuse code from parent classes.

Example: A Vehicle class with child classes like Car, Bike, and Truck.

Encapsulation:

Hiding internal details and exposing only necessary functionality.

Example: A BankAccount class with private attributes like balance.

Polymorphism:

Using the same method name for different behaviors in child classes.

Example: A Shape class with child classes like Circle and Rectangle, each with its own area() method.





Key Differences
Syntax:

Python is more concise and readable compared to C++ and Java.

Example: No semicolons or curly braces in Python.

Memory Management:

Python and Java handle memory automatically, while C++ requires manual memory management.

Inheritance:

Python supports multiple inheritance, while Java uses interfaces to achieve similar functionality.

Typing:

Python is dynamically typed, while C++ and Java are statically typed.


"""