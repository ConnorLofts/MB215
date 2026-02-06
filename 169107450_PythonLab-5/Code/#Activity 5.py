##Activity 5. List Slicing

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic list slicing without specifying start or end
basic_slice = my_list[2:6]
print("Basic slice:", basic_slice)  # Prints [2, 3, 4, 5]

# Slicing from the beginning (start not specified)
start_not_specified = my_list[:4]
print("Slice with start not specified:", start_not_specified)  # Prints [0, 1, 2, 3]

# Slicing until the end (end not specified)
end_not_specified = my_list[7:]
print("Slice with end not specified:", end_not_specified)  # Prints [7, 8, 9]

# Slicing with a step value
step_slice = my_list[1:8:2]
print("Slice with step value:", step_slice)  # Prints [1, 3, 5, 7]

# Slicing using negative indexes (relative to end of list)
negative_indexes = my_list[-5:-1]
print("Slice with negative indexes:", negative_indexes)  # Prints [6, 7, 8]
