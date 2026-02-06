##Activity 4 

list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print("Concatenated list using + operator:", concatenated_list)

# Concatenating lists using the += augmented assignment operator
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1 += list2
print("Concatenated list using += operator:", list1)

# Attempting to concatenate a list with a number (will result in an error)
list1 = [1, 2, 3]
number = 4
concatenated_list = list1 + number


