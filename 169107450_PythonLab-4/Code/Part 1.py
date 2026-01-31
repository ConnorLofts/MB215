# Activity 1: Customizable Dice Simulator

# Part 1: Functions and Randomness

import random

# Activity 1: Customizable Dice Simulator
def roll_dice(num_dice, num_sides):
    total = 0
    for _ in range(num_dice):
        total += random.randint(1, num_sides)
    return total

# Activity 2: Temperature Converter
def convert_temperature(temp, unit):
    if unit.upper() == 'C':
        return (temp * 9/5) + 32 # Convert C to F
    elif unit.upper() == 'F': # Convert F to Ce
        return (temp - 32) * 5/9
    else:
        raise ValueError("Invalid unit. Use 'C' or 'F'.")

# Activity 3: Generate a Single Random Number
def generate_random_number(min_val, max_val): 
    return random.randint(min_val, max_val) # Generate a random integer between min val and max val

# Activity 4: Investment Simulator
def simulate_investment(amount, years, rate_min, rate_max): 
    for _ in range(years): # Simulate each year
        rate = random.uniform(rate_min, rate_max)
        amount *= (1 + rate) # Update amount with interest
    return amount

# Call the above functions to demonstrate the results
if __name__ == "__main__":
    # Dice Simulation
    print("Rolling 3 dice with 6 sides each:", roll_dice(3, 6))
    
    # Temperature Conversion
    print("Converting 100F to Celsius:", convert_temperature(100, 'F'))
    print("Converting 0C to Fahrenheit:", convert_temperature(0, 'C'))
    
    # Generate a Single Random Number
    random_number = generate_random_number(1, 100)
    print(f"The generated random number is: {random_number}")
    
    # Investment Simulation (using example values: $1000 initial, 5 years, rate 1-5%)
    final_amount = simulate_investment(1000, 5, 0.01, 0.05)
    print(f"Final investment value after 5 years: ${final_amount:.2f}")