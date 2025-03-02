import math

# Searching Algorithms in Python

# 1. Linear Search:  Suitable for small to medium-sized unsorted lists.
# Time Complexity: O(n)
def linear_search(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1

# Example usage:  arr = [2, 4, 0, 1, 9] ,  target = 1
# print(linear_search(arr, target))  # Output: 3

# 2. Binary Search
# Use Case: Suitable for large sorted lists.
# Time Complexity: O(log n)
def binary_search(arr, target):
  left, right = 0, len(arr) - 1
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return -1

# Example usage:
# arr = [1, 2, 3, 4, 5]
# target = 3
# print(binary_search(arr, target))  # Output: 2

# 3. Jump Search
# Use Case: Suitable for large sorted lists.
# Time Complexity: O(√n)

def jump_search(arr, target):
  n = len(arr)
  step = int(math.sqrt(n))
  prev = 0

  while arr[min(step, n) - 1] < target:
    prev = step
    step += int(math.sqrt(n))
    if prev >= n:
      return -1

  for i in range(prev, min(step, n)):
    if arr[i] == target:
      return i
  return -1

# Example usage:
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# target = 7
# print(jump_search(arr, target))  # Output: 7

# 4. Interpolation Search
# Use Case: Suitable for uniformly distributed sorted lists.
# Time Complexity: O(log log n)
def interpolation_search(arr, target):
  low = 0
  high = len(arr) - 1

  while low <= high and target >= arr[low] and target <= arr[high]:
    if low == high:
      if arr[low] == target:
        return low
      return -1

    pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

    if arr[pos] == target:
      return pos
    if arr[pos] < target:
      low = pos + 1
    else:
      high = pos - 1

  return -1

# Example usage:
# arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
# target = 18
# print(interpolation_search(arr, target))  # Output: 4

# 5. Exponential Search
# Use Case: Suitable for large sorted lists.
# Time Complexity: O(log n)
def exponential_search(arr, target):
  if arr[0] == target:
    return 0

  n = len(arr)
  i = 1
  while i < n and arr[i] <= target:
    i = i * 2

  return binary_search(arr[:min(i, n)], target)

# Example usage:
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target = 6
# print(exponential_search(arr, target))  # Output: 5








# Linear Search in Python

# Linear Search is a simple searching algorithm that checks each element in the list
# sequentially until the target element is found.

def linear_search(arr, target):
    """
    Searches for a target element in a list using Linear Search.
    
    :param arr: List of elements to search.
    :param target: Element to search for.
    :return: Index of the target element if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if found
    return -1  # Return -1 if not found

# Use Case: Searching for an element in a small list
numbers = [10, 20, 30, 40, 50]
target = 30
index = linear_search(numbers, target)
print(f"Element {target} found at index:", index)

# Time Complexity: O(n) (inefficient for large datasets)
# Space Complexity: O(1) (in-place search)









# Binary Search in Python

# Binary Search is an efficient searching algorithm that works on sorted lists.
# It repeatedly divides the list in half and compares the middle element with the target.

def binary_search(arr, target):
    """
    Searches for a target element in a sorted list using Binary Search.
    
    :param arr: Sorted list of elements to search.
    :param target: Element to search for.
    :return: Index of the target element if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        if arr[mid] == target:
            return mid  # Return the index if found
        elif arr[mid] < target:
            low = mid + 1  # Search the right half
        else:
            high = mid - 1  # Search the left half
    return -1  # Return -1 if not found

# Use Case: Searching for an element in a large sorted list
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 60
index = binary_search(numbers, target)
print(f"Element {target} found at index:", index)

# Time Complexity: O(log n) (efficient for large datasets)
# Space Complexity: O(1) (in-place search)