# Activity 2: Temperature Converter
def convert_temperature(temp, unit):
    
# Add the missing code here. Can use the following formulas to do #the do #conversion
    if unit == "C":
        return (temp * 9/5) + 32  # Celsius to Fahrenheit
    elif unit == "F":
        return (temp - 32) * 5/9  # Fahrenheit to Celsius
    else:
        return "Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit."
     
 
