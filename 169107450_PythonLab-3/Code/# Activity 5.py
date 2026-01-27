# Activity 5
import keyboard
Number_added = int(input("Enter a number to add to your sum: "))
Sum = 0
while Sum < 100:
    Sum = Sum + Number_added
    if Sum < 100:
        Number_added = int(input(f"Enter another number to add to your sum. Your current sum is {Sum}: "))
    elif keyboard.is_Pressed ("space"):
        break
# Displaying the result 
print(f"The total sum is: {Sum}")
