import traceback

# Activity 1: Writing to a File. This code is provided to you to show how #to write to a file, the use if try except for exception handling and the #use of traceback
def write_to_file(filename, data):
    try:
        with open(filename, 'w') as file: 
            file.write(data)
    except Exception as e:
        print(f"An error occurred while writing to the file: {filename}")
        traceback.print_exc()

# Activity 2: Reading from a File
def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"An error occurred while reading from the file: {filename}")
        traceback.print_exc()
        return None

# Activity 3: Appending to a File
def append_to_file(filename, data):
    try:
        with open(filename, 'a') as file:
            file.write(data)
    except Exception as e:
        print(f"An error occurred while appending to the file: {filename}")
        traceback.print_exc()

# Demonstrating the functions
if __name__ == "__main__":
    # Writing to a file
    write_to_file('sample.txt', 'Test\n')
    
    # Reading from a file
    content = read_from_file('sample.txt')
    if content is not None:
        print("Content after writing:")
        print(content)
    
    # Appending to a file
    append_to_file('sample.txt', 'Appended line.\n')
    content = read_from_file('sample.txt')
    if content is not None:
        print("Content after appending:")
        print(content)
    
# Trying to read from a non-existent file to demonstrate exception handling
    non_existent_content = read_from_file('non_existent_file.txt')
    if non_existent_content is None:
        print("Could not read the non-existent file.")