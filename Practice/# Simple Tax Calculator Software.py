
# Activity 6: Demonstrating 'for' loops

# Part 1: For loop with range() to print even numbers (e.g., from 0 to 10, excluding 10)
print("Even numbers from 0 to 8:")
for num in range(0, 10, 2):
    print(num, end=' ')
print("\n")

# Part 2: Nested for loop to print a multiplication table for 1 to 3 multiplied by 1 to 10
print("Multiplication table for 1 to 3:")
for i in range(1, 4):  # Outer loop: 1 to 3
    for j in range(1, 11):  # Inner loop: 1 to 10
        print(f"{i} * {j} = {i * j}", end='\t')
    print()  # New line after each row
print()

# Part 3: For loop to reverse the characters of a given string and print them
given_string = "Hello, World!"  # Example string
print(f"Original string: {given_string}")
print("Reversed string characters:")
for i in range(len(given_string) - 1, -1, -1):
    print(given_string[i], end='')
print("\n")