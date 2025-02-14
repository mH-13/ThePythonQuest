"""
Sorting Algorithms in Python

This module contains implementations of various sorting algorithms in Python.
Each algorithm is implemented as a function that takes a list as input and returns a sorted list.
"""

def bubble_sort(arr):
  """
  Bubble Sort Algorithm
  Time Complexity: O(n^2)
  Space Complexity: O(1)

  Use Case:
  - Simple to implement and understand.
  - Suitable for small datasets or nearly sorted datasets.
  - Not suitable for large datasets due to its quadratic time complexity.

  :param arr: List of elements to be sorted
  :return: Sorted list
  """
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

def selection_sort(arr):
  """
  Selection Sort Algorithm
  Time Complexity: O(n^2)
  Space Complexity: O(1)

  Use Case:
  - Simple to implement and understand.
  - Suitable for small datasets.
  - Performs well on lists with a small number of elements.

  :param arr: List of elements to be sorted
  :return: Sorted list
  """
  n = len(arr)
  for i in range(n):
    min_idx = i
    for j in range(i+1, n):
      if arr[j] < arr[min_idx]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  return arr

def insertion_sort(arr):
  """
  Insertion Sort Algorithm
  Time Complexity: O(n^2)
  Space Complexity: O(1)

  Use Case:
  - Simple to implement and understand.
  - Efficient for small datasets or nearly sorted datasets.
  - Performs well on lists that are already partially sorted.

  :param arr: List of elements to be sorted
  :return: Sorted list
  """
  for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key
  return arr

def merge_sort(arr):
  """
  Merge Sort Algorithm
  Time Complexity: O(n log n)
  Space Complexity: O(n)

  Use Case:
  - Suitable for large datasets.
  - Stable sort (maintains the relative order of equal elements).
  - Performs well on linked lists and external sorting.

  :param arr: List of elements to be sorted
  :return: Sorted list
  """
  if len(arr) > 1:
    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]

    merge_sort(L)
    merge_sort(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        arr[k] = L[i]
        i += 1
      else:
        arr[k] = R[j]
        j += 1
      k += 1

    while i < len(L):
      arr[k] = L[i]
      i += 1
      k += 1

    while j < len(R):
      arr[k] = R[j]
      j += 1
      k += 1
  return arr

def quick_sort(arr):
  """
  Quick Sort Algorithm
  Time Complexity: O(n log n)
  Space Complexity: O(log n)

  Use Case:
  - Suitable for large datasets.
  - Performs well in practice with average-case time complexity of O(n log n).
  - Not stable (does not maintain the relative order of equal elements).

  :param arr: List of elements to be sorted
  :return: Sorted list
  """
  if len(arr) <= 1:
    return arr
  else:
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def heap_sort(arr):
  """
  Heap Sort Algorithm
  Time Complexity: O(n log n)
  Space Complexity: O(1)

  Use Case:
  - Suitable for large datasets.
  - Performs well with a guaranteed time complexity of O(n log n).
  - Not stable (does not maintain the relative order of equal elements).

  :param arr: List of elements to be sorted
  :return: Sorted list
  """
  def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
      largest = l

    if r < n and arr[largest] < arr[r]:
      largest = r

    if largest != i:
      arr[i], arr[largest] = arr[largest], arr[i]
      heapify(arr, n, largest)

  n = len(arr)

  for i in range(n // 2 - 1, -1, -1):
    heapify(arr, n, i)

  for i in range(n-1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, i, 0)

  return arr







#deepseek
# Bubble Sort in Python

# Bubble Sort is a simple sorting algorithm that repeatedly steps through the list,
# compares adjacent elements, and swaps them if they are in the wrong order.

def bubble_sort(arr):
    """
    Sorts a list using the Bubble Sort algorithm.
    
    :param arr: List of elements to sort.
    :return: Sorted list.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
    return arr

# Use Case: Sorting a small list of numbers
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print("Sorted Numbers (Bubble Sort):", sorted_numbers)

# Time Complexity: O(n²) (inefficient for large datasets)
# Space Complexity: O(1) (in-place sorting)







# Merge Sort in Python

# Merge Sort is a divide-and-conquer algorithm that divides the input array into two halves,
# sorts them recursively, and then merges the two sorted halves.

def merge_sort(arr):
    """
    Sorts a list using the Merge Sort algorithm.
    
    :param arr: List of elements to sort.
    :return: Sorted list.
    """
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle point
        left_half = arr[:mid]  # Divide the array into two halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Recursively sort the left half
        merge_sort(right_half)  # Recursively sort the right half

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements in the left half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Check for any remaining elements in the right half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Use Case: Sorting a large list of numbers
numbers = [38, 27, 43, 3, 9, 82, 10]
sorted_numbers = merge_sort(numbers)
print("Sorted Numbers (Merge Sort):", sorted_numbers)

# Time Complexity: O(n log n) (efficient for large datasets)
# Space Complexity: O(n) (requires additional space for merging)