#This script demonstrates how to write to a file in Python.

#Writes the given content to a file specified by file_path.
#file_path (str): The path to the file where the content will be written/append.
#content (str): The content to write/append to the file.
#If an error occurs during the operation, an error message will be displayed.
#The function does not return any value.
#Note: If the file does not exist, it will be created.


#If the file exists, its content will be overwritten.
def write_to_file(file_path, content):
  try:
    with open(file_path, 'w') as file:
      file.write(content)
    print(f"Content successfully written to {file_path}")
  except Exception as e:
    print(f"An error occurred while writing to the file: {e}")


#If the file exists, the content will be appended to the end of the file.
def append_to_file(file_path, content):

  try:
    with open(file_path, 'a') as file:
      file.write(content)
    print(f"Content successfully appended to {file_path}")
  except Exception as e:
    print(f"An error occurred while appending to the file: {e}")

if __name__ == "__main__":
  # Example usage
  file_path = 'example.txt'
  content_to_write = "Hello, this is a test content.\n"
  content_to_append = "This is additional content.\n"

  write_to_file(file_path, content_to_write)
  append_to_file(file_path, content_to_append)
  
  
  
  
  
  
  



# Writing to a File in Python

# Example 1: Writing to a File
# Use Case: Saving user input or program output to a file
with open("output.txt", "w") as file:  # Open file in write mode
    file.write("Hello, World!\n")  # Write a single line
    file.write("This is a Python file handling example.\n")

# Example 2: Appending to a File
# Use Case: Adding new data to an existing file (e.g., logs or records)
with open("output.txt", "a") as file:  # Open file in append mode
    file.write("Appending a new line.\n")

# Example 3: Writing Multiple Lines
# Use Case: Writing a list of data to a file (e.g., saving a to-do list)
lines = ["Task 1: Buy groceries\n", "Task 2: Pay bills\n", "Task 3: Call mom\n"]
with open("tasks.txt", "w") as file:
    file.writelines(lines)  # Write all lines at once

# Example 4: Writing JSON Data
# Use Case: Saving structured data (e.g., configurations or user data)
import json

data = {
    "name": "Alice",
    "age": 25,
    "is_student": True,
    "courses": ["Math", "Physics"]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)  # Write JSON data with indentation

# Example 5: Writing CSV Data
# Use Case: Saving tabular data (e.g., spreadsheets or reports)
import csv

data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "London"],
    ["Charlie", 35, "Paris"]
]

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)  # Write all rows at once

# Example 6: Overwriting vs Appending
# Use Case: Choosing between overwriting or adding to a file
with open("log.txt", "w") as file:  # Overwrite the file
    file.write("Log Entry 1\n")

with open("log.txt", "a") as file:  # Append to the file
    file.write("Log Entry 2\n")
    
    
    
# Use Cases for File Handling
# Reading Files:

# Loading configuration files for applications.

# Processing large datasets or log files line by line.

# Extracting specific information from files (e.g., headers or metadata).

# Writing Files:

# Saving program output or user input to a file.

# Logging events or errors in an application.

# Storing structured data like JSON or CSV for later use.

# Appending to Files:

# Adding new entries to log files or records.

# Updating existing files without overwriting their content.

# Error Handling:

# Gracefully handling missing files or incorrect file paths.

# Ensuring files are properly closed after use.