"""A queue is a linear data structure that follows the First In First Out (FIFO) principle. 
Elements are added from the rear and removed from the front.

Use Cases:
1. Task scheduling
2. Handling of asynchronous data (e.g., IO Buffers)
3. Breadth-First Search (BFS) in graph algorithms
4. Print job management

Complexity:
- Enqueue (add an element): O(1)
- Dequeue (remove an element): O(1)
- Peek (get the front element): O(1)
- isEmpty (check if the queue is empty): O(1)
"""

class Queue:
  def __init__(self):
    self.items = [] # Initialize an empty queue. 

  def is_empty(self): # Check if the queue is empty. 
    return len(self.items) == 0 # Return True if the queue is empty, False otherwise.

  
  def enqueue(self, item): # Add an item to the rear of the queue. Args: item: The item to be added to the queue.
    self.items.append(item) # Append the item to the end of the list. 
    # The time complexity is O(1) because it takes constant time to add an element to the end of the list.

  
  def dequeue(self): # Remove and return the front item of the queue. 
    if self.is_empty():
      raise IndexError("dequeue from empty queue")
    return self.items.pop(0)  # Remove and return the first item from the list. The time complexity is O(n) because all elements are shifted by one. 
  #A better approach is to use collections.deque.  It provides an optimized way to add and remove elements from both ends of the list. 
  
  # To use deque, import it from the collections module and initialize it as follows:
  from collections import deque
  #self.items = deque()
  #The enqueue and dequeue methods can be modified as follows:
  def enqueue(self, item):
    self.items.append(item)
  def dequeue(self):
    if self.is_empty():
      raise IndexError("dequeue from empty queue")
    return self.items.popleft() # Use popleft() to remove and return the first item from the deque.
  # The time complexity of deque is O(1) for append and pop operations.

  def peek(self): # Get the front item of the queue without removing it.
    if self.is_empty():
      raise IndexError("peek from empty queue")
    return self.items[0] # Return the first item in the list. The item at the front of the queue.

  def size(self):

    return len(self.items) # Return the number of items in the list.

# Example usage:
if __name__ == "__main__":
  q = Queue()
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)
  print(q.dequeue())  # Output: 1
  print(q.peek())     # Output: 2
  print(q.size())     # Output: 2
  print(q.is_empty()) # Output: False
  q.dequeue()
  q.dequeue()
  print(q.is_empty()) # Output: True
  
  
  
  
  
  
  

  
  # Queue in Python:  First-In-First-Out (FIFO) data structure.
# It supports two main operations: enqueue (add an element) and dequeue (remove the front element).

from collections import deque

class Queue:
    def __init__(self): # Constructor to initialize the queue.
        """Initialize an empty queue."""
        self.items = deque() # Use deque to store the elements. initialize an empty deque.

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the front item from the queue."""
        if not self.is_empty():
            return self.items.popleft()
        return None  # Return None if the queue is empty

    def peek(self):
        """Return the front item without removing it."""
        if not self.is_empty():
            return self.items[0]
        return None  # Return None if the queue is empty

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

# Use Case: Managing tasks in a print queue
queue = Queue()
queue.enqueue("Task 1")
queue.enqueue("Task 2")
print("Front of Queue:", queue.peek())  # Task 1
queue.dequeue()
print("Front of Queue after Dequeue:", queue.peek())  # Task 2