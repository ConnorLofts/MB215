# main.py

from car import Car
#Creating 2 cars 
car1 = Car("Tesla", "Model 3", 2022)
car2 = Car("Rivian", "R1T", 2024)

print("Car Information")
print("Car 1:")
car1.display_info()

print("Car 2:")
car2.display_info()

#Updating model 

print("Updating Car 1 Model")
car1.update_model("Model Y")

print("After update - Car 1:")
car1.display_info()

# Using __str__ method
print("String Representation")
print("Car 1", car1)
print("Car 2", car2)

# Compare car years
def compare_car_years(car1, car2):
    
    if car1.year < car2.year:
        return f"{car1} is older than {car2}"
    elif car1.year > car2.year:
        return f"{car1} is newer than {car2}"
    else:
        return f"{car1} and {car2} are from the same year ({car1.year})"

print("Year Comparison")
print(compare_car_years(car1, car2))