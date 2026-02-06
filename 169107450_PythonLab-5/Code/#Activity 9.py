#Activity 9. 

original_list = [1, 2, 3, 4, 5]

copied_list1 = []
for item in original_list:
    copied_list1.append(item)

print("Method 1: Copied list using a for loop:", copied_list1)

original_list = [1, 2, 3, 4, 5]

copied_list2 = [] + original_list


print("Method 2: Copied list using concatenation:", copied_list2)

original_list = [1, 2, 3, 4, 5]

copied_list = list(original_list)

total = sum(item for item in copied_list)

average = total / len(copied_list) if copied_list else 0

print("Total of numeric values in the copied list:", total)
print("Average of numeric values in the copied list:", average)
