# various ways to read files in Python.

# read the entire file at once
# This method is useful for small files
# as it reads the entire file into memory
# and returns the content as a string
# This is known as eager loading
# as the entire file is loaded into memory at once
# which can be inefficient for large files 
# as it consumes a lot of memory
# and may slow down the program
# if the file is too large to fit into memory  
def read_entire_file(file_path):

  with open(file_path, 'r') as file: 
    content = file.read()
    
  return content # Returns the content of the file as a string

# read the file line by line
# This method is useful for small files
# as it reads the entire file into memory
# and returns a list of lines
def read_file_by_lines(file_path):

  with open(file_path, 'r') as file:
    lines = file.readlines()
    
  return lines # Returns a list of lines from the file

# read the file line by line using a loop
# This method is useful for large files
# as it reads the file line by line without loading the entire file into memory
# This is known as lazy loading or lazy evaluation 
def read_file_line_by_line(file_path):

  with open(file_path, 'r') as file:
    for line in file:
      print(line, end='')


# read the file using a context manager
# This method is useful for ensuring proper resource management
# as it automatically closes the file after reading
# This is known as the with statement or context manager 
# which ensures that the file is properly closed even if an exception occurs 
# This is a common practice in Python to avoid resource leaks
# and ensure that resources are released properly
# after they are no longer needed
# This is known as the RAII (Resource Acquisition Is Initialization) pattern
# which is a common idiom in Python for managing resources
def read_file_with_context_manager(file_path):

  with open(file_path, 'r') as file:
    content = file.read()
    
  return content # Returns the content of the file as a string



# read the file in binary mode
# This method is useful for reading non-text files
# such as images, audio, video, etc.
# as it reads the file as bytes
# This is known as reading in binary mode 
# which is useful for reading non-text files
# as it preserves the original binary data
# without any encoding or decoding
# This is useful for reading files that are not in text format
# such as images, audio, video, etc.
def read_file_in_binary_mode(file_path):

  with open(file_path, 'rb') as file:
    content = file.read()
    
  return content # Returns the content of the file as bytes

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