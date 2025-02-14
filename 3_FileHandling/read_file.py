"""
This script demonstrates various ways to read files in Python.
"""

def read_entire_file(file_path):
  """
  Reads the entire content of a file.
  
  :param file_path: Path to the file to be read.
  :return: Content of the file as a string.
  """
  with open(file_path, 'r') as file:
    content = file.read()
  return content

def read_file_by_lines(file_path):
  """
  Reads a file line by line.
  
  :param file_path: Path to the file to be read.
  :return: List of lines from the file.
  """
  with open(file_path, 'r') as file:
    lines = file.readlines()
  return lines

def read_file_line_by_line(file_path):
  """
  Reads a file line by line using a loop.
  
  :param file_path: Path to the file to be read.
  """
  with open(file_path, 'r') as file:
    for line in file:
      print(line, end='')

def read_file_with_context_manager(file_path):
  """
  Reads a file using a context manager to ensure proper resource management.
  
  :param file_path: Path to the file to be read.
  :return: Content of the file as a string.
  """
  with open(file_path, 'r') as file:
    content = file.read()
  return content

def read_file_in_binary_mode(file_path):
  """
  Reads a file in binary mode.
  
  :param file_path: Path to the file to be read.
  :return: Content of the file as bytes.
  """
  with open(file_path, 'rb') as file:
    content = file.read()
  return content

# Example usage:
if __name__ == "__main__":
  file_path = 'example.txt'
  
  # Read entire file
  print("Reading entire file:")
  print(read_entire_file(file_path))
  
  # Read file by lines
  print("\nReading file by lines:")
  lines = read_file_by_lines(file_path)
  for line in lines:
    print(line, end='')
  
  # Read file line by line
  print("\n\nReading file line by line:")
  read_file_line_by_line(file_path)
  
  # Read file with context manager
  print("\n\nReading file with context manager:")
  print(read_file_with_context_manager(file_path))
  
  # Read file in binary mode
  print("\nReading file in binary mode:")
  print(read_file_in_binary_mode(file_path))
  
  
  
  
  
  



# Reading from a File in Python

# File handling allows you to read and write data to files on your system.

# Example 1: Reading an Entire File
# Use Case: Reading a configuration file or a text document
with open("example.txt", "r") as file:  # Open file in read mode
    content = file.read()  # Read the entire content
    print("File Content:\n", content)

# Example 2: Reading Line by Line
# Use Case: Processing a large file line by line (e.g., log files)
with open("example.txt", "r") as file:
    print("Reading Line by Line:")
    for line in file:
        print(line.strip())  # strip() removes extra newline characters

# Example 3: Reading All Lines into a List
# Use Case: Storing lines of a file in a list for further processing
with open("example.txt", "r") as file:
    lines = file.readlines()  # Read all lines into a list
    print("Lines List:", lines)

# Example 4: Reading Specific Lines
# Use Case: Extracting specific information from a file (e.g., headers)
with open("example.txt", "r") as file:
    first_line = file.readline()  # Read the first line
    second_line = file.readline()  # Read the second line
    print("First Line:", first_line.strip())
    print("Second Line:", second_line.strip())

# Example 5: Using 'with' Statement
# The 'with' statement automatically closes the file after the block is executed.
# Use Case: Ensuring proper file handling and avoiding resource leaks
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content (with 'with'):\n", content)

# Example 6: Handling File Not Found Error
# Use Case: Gracefully handling missing files in an application
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")