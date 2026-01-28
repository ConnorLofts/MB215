# Activity 6

# For loop with range to print even numbers from 2 to 20
print("Even numbers from 2 to 20:")
for num in range(2, 21, 2):
    print(num, end=' ')
print("\n")

# Nested for loop to create a multiplication table for numbers 1 to 3
print("Multiplication table for numbers 1 to 3:")
for i in range(1, 4):  # Outer loop: 1 to 3
    for j in range(1, 11):  # Inner loop: 1 to 10
        print(f"{i} * {j} = {i * j}", end='\t')
    print()  # New line after each row
print()

# For loop to reverse a string. Note: Use ‘reversed’ keyword
given_string = "Hello"
print(f"Reversing the string '{given_string}':")
for char in reversed(given_string):
    print(char, end=' ')
print()