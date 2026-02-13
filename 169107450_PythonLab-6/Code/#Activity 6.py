#Activity 6.


my_list = [10, 20, 30, 40, 50]

item_to_check = 30
if item_to_check in my_list:
    print(f"{item_to_check} is in the list.")
else:
    print(f"{item_to_check} is not in the list.")

item_to_check = 60
if item_to_check not in my_list:
    print(f"{item_to_check} is not in the list.")
else:
    print(f"{item_to_check} is in the list.")

