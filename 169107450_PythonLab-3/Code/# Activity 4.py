# Activity 4
# Step 1: Declare two Boolean variables
is_true = True
is_false = False

# Step 2: Demonstrate logical operations (AND, OR, NOT)
# Logical AND
print("True AND False:", is_true and is_false)

# Logical OR
print("True OR False:", is_true or is_false)

# Logical NOT
print("NOT True:", not is_true)
print("NOT False:", not is_false)

# Step 3: Use a Boolean variable in a conditional statement
# Conditional statement with logical operation
if is_true and not is_false:
    print("The condition (True AND NOT False) is met.")
else:
    print("The condition (True AND NOT False) is not met.")