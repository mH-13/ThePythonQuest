class Stack:
  """
  A simple implementation of a stack data structure in Python.

  A stack is a collection of elements with two principal operations:
  - push, which adds an element to the collection, and
  - pop, which removes the most recently added element that was not yet removed.

  This implementation uses a list to store the stack elements.

  Methods:
    __init__():
      Initializes an empty stack.
    
    is_empty() -> bool:
      Checks if the stack is empty.
      Returns True if the stack is empty, False otherwise.
    
    push(item):
      Adds an item to the top of the stack.
    
    pop() -> any:
      Removes and returns the item at the top of the stack.
      Raises IndexError if the stack is empty.
    
    peek() -> any:
      Returns the item at the top of the stack without removing it.
      Raises IndexError if the stack is empty.
    
    size() -> int:
      Returns the number of items in the stack.

  Use case example:

  Complexity:
    - is_empty: O(1)
    - push: O(1)
    - pop: O(1)
    - peek: O(1)
    - size: O(1)
  """
  def __init__(self):
    self.items = []

  def is_empty(self):
    return len(self.items) == 0

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if self.is_empty():
      raise IndexError("pop from empty stack")
    return self.items.pop()

  def peek(self):
    if self.is_empty():
      raise IndexError("peek from empty stack")
    return self.items[-1]

  def size(self):
    return len(self.items)

# Use case example
if __name__ == "__main__":
  stack = Stack()
  stack.push(1)
  stack.push(2)
  stack.push(3)
  print(stack.pop())  # Output: 3
  print(stack.peek())  # Output: 2
  print(stack.size())  # Output: 2

# Complexity:
# - is_empty: O(1)
# - push: O(1)
# - pop: O(1)
# - peek: O(1)
# - size: O(1)



# Stack in Python

# A Stack is a Last-In-First-Out (LIFO) data structure.
# It supports two main operations: push (add an element) and pop (remove the top element).

class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item from the stack."""
        if not self.is_empty():
            return self.items.pop()
        return None  # Return None if the stack is empty

    def peek(self):
        """Return the top item without removing it."""
        if not self.is_empty():
            return self.items[-1]
        return None  # Return None if the stack is empty

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

# Use Case: Implementing undo/redo functionality in a text editor
stack = Stack()
stack.push("Action 1")
stack.push("Action 2")
print("Top of Stack:", stack.peek())  # Action 2
stack.pop()
print("Top of Stack after Pop:", stack.peek())  # Action 1