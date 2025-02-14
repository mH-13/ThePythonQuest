class Node:
  """
  A Node in a linked list.

  Attributes:
    data: The data stored in the node.
    next_node: The reference to the next node in the linked list.
  """
  def __init__(self, data):
    self.data = data
    self.next_node = None


class LinkedList:
  """
  A singly linked list.

  Methods:
    insert_at_beginning(data): Inserts a new node with the given data at the beginning of the list.
    insert_at_end(data): Inserts a new node with the given data at the end of the list.
    delete_node(data): Deletes the first node with the given data.
    search(data): Searches for a node with the given data.
    display(): Displays the entire linked list.
  """
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next_node = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      return
    last_node = self.head
    while last_node.next_node:
      last_node = last_node.next_node
    last_node.next_node = new_node

  def delete_node(self, data):
    current_node = self.head
    if current_node and current_node.data == data:
      self.head = current_node.next_node
      current_node = None
      return
    prev_node = None
    while current_node and current_node.data != data:
      prev_node = current_node
      current_node = current_node.next_node
    if current_node is None:
      return
    prev_node.next_node = current_node.next_node
    current_node = None

  def search(self, data):
    current_node = self.head
    while current_node:
      if current_node.data == data:
        return True
      current_node = current_node.next_node
    return False

  def display(self):
    nodes = []
    current_node = self.head
    while current_node:
      nodes.append(current_node.data)
      current_node = current_node.next_node
    print(" -> ".join(map(str, nodes)))


# Use cases
if __name__ == "__main__":
  linked_list = LinkedList()
  linked_list.insert_at_beginning(3)
  linked_list.insert_at_beginning(2)
  linked_list.insert_at_end(4)
  linked_list.insert_at_end(5)
  linked_list.display()  # Output: 2 -> 3 -> 4 -> 5

  linked_list.delete_node(3)
  linked_list.display()  # Output: 2 -> 4 -> 5

  print(linked_list.search(4))  # Output: True
  print(linked_list.search(3))  # Output: False

# Complexity Analysis:
# - Insertion at the beginning: O(1)
# - Insertion at the end: O(n)
# - Deletion: O(n)
# - Search: O(n)
# - Display: O(n)



# Linked List in Python

# A Linked List is a linear data structure where each element (node) contains data and a reference to the next node.

class Node:
    def __init__(self, data):
        """Initialize a node with data and a reference to the next node."""
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def append(self, data):
        """Add a node with data to the end of the linked list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        """Add a node with data to the beginning of the linked list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self, data):
        """Delete the first node with the given data."""
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def print_list(self):
        """Print all elements in the linked list."""
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Use Case: Implementing a playlist where songs are added and removed
playlist = LinkedList()
playlist.append("Song 1")
playlist.append("Song 2")
playlist.prepend("Song 0")
playlist.print_list()  # Song 0 -> Song 1 -> Song 2 -> None
playlist.delete_with_value("Song 1")
playlist.print_list()  # Song 0 -> Song 2 -> None