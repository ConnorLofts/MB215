#Activity 7: Working with Multiple Instances and Passing Objects as Arguments
#In main.py, create a function that compares two Car objects based on their year. Instantiate two Car objects and use this function to compare them.
from car import Car
def compare_car_years(car1, car2):
    return car1.year < car2.year

# Your code here to define with values and print the comparison output
car1 = Car("Tesla", "Model 3", 2022)
car2 = Car("Rivian", "R1T", 2024)

if compare_car_years(car1, car2):
    print(f"{car1} is older than {car2}")
else:
    print(f"{car1} is not older than {car2}")