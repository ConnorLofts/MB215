# Activity 6

a = float(input("Enter a Value for A:"))
b = float(input("Enter a Value for B:"))

addition = a + b
print("Addition:", addition)

subtraction = a - b
print("Subtraction:", subtraction)

multiplication = a * b
print("Multiplication:", multiplication)

if b != 0:
    division = a / b
    print("Division:", division)

    integer_division = a // b
    print("Integer Division:", integer_division)
    remainder = a % b
    print("Remainder:", remainder)
else:
    print("Cannot perform division, integer division or remainder because b is zero.")

exponent = a ** b
print("Exponent:", exponent)

