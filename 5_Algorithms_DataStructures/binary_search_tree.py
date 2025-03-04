class TreeNode:
  """A node in the binary search tree.
  
  Attributes:
  -----------
  key : int
    The value of the node.
  left : TreeNode
    The left child node.
  right : TreeNode
    The right child node.
  """
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

class BinarySearchTree:
  """ A binary search tree (BST) implementation.
  
  Methods:
  --------
  insert(key)
    Inserts a new node with the given key.
  search(key)
    Searches for a node with the given key.
  delete(key)
    Deletes a node with the given key.
  inorder_traversal()
    Performs an in-order traversal of the tree.
  """
  def __init__(self):
    self.root = None

  def insert(self, key):
    """ Inserts a new node with the given key into the BST.
    
    Parameters:
    -----------
    key : int
      The value to insert into the BST.
    """
    if self.root is None:
      self.root = TreeNode(key)
    else:
      self._insert(self.root, key)

  def _insert(self, node, key):
    if key < node.key:
      if node.left is None:
        node.left = TreeNode(key)
      else:
        self._insert(node.left, key)
    else:
      if node.right is None:
        node.right = TreeNode(key)
      else:
        self._insert(node.right, key)

  def search(self, key):
    """Searches for a node with the given key in the BST.
    
    Parameters:
    -----------
    key : int
      The value to search for in the BST.
    
    Returns:
    --------
    TreeNode or None
      The node with the given key, or None if not found.
    """
    return self._search(self.root, key)

  def _search(self, node, key):
    if node is None or node.key == key:
      return node
    if key < node.key:
      return self._search(node.left, key)
    return self._search(node.right, key)

  def delete(self, key):
    """Deletes a node with the given key from the BST.
    
    Parameters:
    -----------
    key : int
      The value to delete from the BST.
    """
    self.root = self._delete(self.root, key)

  def _delete(self, node, key):
    if node is None:
      return node
    if key < node.key:
      node.left = self._delete(node.left, key)
    elif key > node.key:
      node.right = self._delete(node.right, key)
    else:
      if node.left is None:
        return node.right
      elif node.right is None:
        return node.left
      temp = self._min_value_node(node.right)
      node.key = temp.key
      node.right = self._delete(node.right, temp.key)
    return node

  def _min_value_node(self, node):
    current = node
    while current.left is not None:
      current = current.left
    return current

  def inorder_traversal(self):
    """
    Performs an in-order traversal of the BST.
    
    Returns:
    --------
    list
      A list of node keys in in-order.
    """
    result = []
    self._inorder_traversal(self.root, result)
    return result

  def _inorder_traversal(self, node, result):
    if node:
      self._inorder_traversal(node.left, result)
      result.append(node.key)
      self._inorder_traversal(node.right, result)

# Use cases:
# 1. Insert elements into the BST.
# 2. Search for elements in the BST.
# 3. Delete elements from the BST.
# 4. Perform in-order traversal to get elements in sorted order.

# Complexity:
# - Insertion: O(h), where h is the height of the tree.
# - Search: O(h), where h is the height of the tree.
# - Deletion: O(h), where h is the height of the tree.
# - In-order Traversal: O(n), where n is the number of nodes in the tree.




# Binary Search Tree (BST) in Python

# A BST is a tree data structure where each node has at most two children.
# For any given node:
# - All elements in the left subtree are less than the node's value.
# - All elements in the right subtree are greater than the node's value.

class TreeNode:
    def __init__(self, key):
        """Initialize a tree node with a key and left/right children."""
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        """Initialize an empty BST."""
        self.root = None

    def insert(self, key):
        """Insert a key into the BST."""
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        """Helper function to insert a key recursively."""
        if key < node.key:
            if not node.left:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if not node.right:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        """Search for a key in the BST."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        """Helper function to search for a key recursively."""
        if not node or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def inorder_traversal(self):
        """Perform an inorder traversal of the BST."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """Helper function for inorder traversal."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

# Use Case: Storing and searching for data in a sorted manner
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
print("Inorder Traversal:", bst.inorder_traversal())  # [3, 5, 7, 10, 15]
print("Search for 7:", bst.search(7) is not None)  # True