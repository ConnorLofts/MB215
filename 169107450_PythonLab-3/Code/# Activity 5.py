# Activity 5

total_sum = 0
count = 0

# The sum should not exceed 100
while total_sum < 100:
    user_input = input("Enter a number or a space (' ') to exit: ")

    # If the user enters a space, break out of the loop
    if user_input == ' ':
        break

    # Add the number to the sum and add 1 to the count
    try:
        number = int(user_input)
        total_sum += number
        count += 1
    except ValueError:
        print("Invalid input. Please enter a number or a space.")

# Display the total sum and the count
print(f"The total sum is: {total_sum}")
print(f"The count of numbers added is: {count}")
 