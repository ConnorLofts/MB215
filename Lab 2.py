# Activity 1
import datetime

# Write a program that asks for the user's name and age.
name = input("Please enter your name")
age = input("Please enter your age")

# Print a greeting and calculate the year the user was born
age = int(age)
current_year = datetime.datetime.now().year
birth_year = current_year - age
print(f"You were born in {birth_year}")
print(f"Greetings {name}")

 # Activity 2

length = float(input("Please enter the length"))

width = float(input("Please enter the width"))  

area = length * width

print(f"The area of the rectangle is {area}")

# Activity 3


string1 = input("Enter the first string: ")

string2 = input("Enter the second string: ")

string3 = input("Enter the third string: ")

# Concatenate them into a full sentence with spaces
full_sentence = string1 + " " + string2 + " " + string3 + "."

print(f"{full_sentence}")

# Activity 4


