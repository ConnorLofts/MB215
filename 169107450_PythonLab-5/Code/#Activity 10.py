# Activity 10.
def save_list_to_file(file_name, input_list):
    with open(file_name, 'w') as file:
        file.writelines(f"{item}\n" for item in input_list)

def read_list_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

original_list = ['Apple', 'Banana', 'Cherry', 'Date']

file_name = 'fruits.txt'

save_list_to_file(file_name, original_list)

read_data = read_list_from_file(file_name)

print("Data read from the file:", read_data)

