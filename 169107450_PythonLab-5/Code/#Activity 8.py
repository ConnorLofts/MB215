#Activity 8. 

my_list = [10, 30, 20, 40, 20]
print("initial list: ", my_list)

my_list.append(50)
my_list.append(20) 
print("The list after appending elements 50 & 20: ", my_list)

my_list.insert(2, 25)


my_list.sort()
print("print the list after sorting: ", my_list)

item_to_count = 20
count_result = my_list.count(item_to_count)
print(f"The item {item_to_count} appears {count_result} times in the list.")

item_to_find = 20
try:
    index_result = my_list.index(item_to_find)
    print(f"The first occurrence of {item_to_find} is at index {index_result}.")
except ValueError:
    print(f"{item_to_find} is not in the list.")

item_to_remove = 20
my_list.remove(item_to_remove)
print("print the list after removing 20: ", my_list)

my_list.reverse()
print("print the list after reversing: ", my_list)

index_to_delete = 2
del my_list[index_to_delete]
print("print the list after deleting item at index 2 ", my_list)

list_sum = sum(my_list)

list_min = min(my_list)
list_max = max(my_list)


print("Updated list:", my_list)
print(f"Sum of elements: {list_sum}")
print(f"Minimum value: {list_min}")
print(f"Maximum value: {list_max}")

