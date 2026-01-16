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