# Activity 1
import datetime

# Asking for user's for their name and age.
name = input("Please enter your name")
age = input("Please enter your age")

# Calculating the year the user was born
age = int(age)
current_year = datetime.datetime.now().year
birth_year = current_year - age

# Printing a greeting and calculate the year the user was born
print(f"You were born in {birth_year}")
print(f"Greetings {name}")