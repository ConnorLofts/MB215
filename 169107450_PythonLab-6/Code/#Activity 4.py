#Activity 4: The __str__ Method
#Implement the __str__ method to define a string representation for the #Car class instances.
class Car:
    # Existing methods and __init__# car.py (updated)
    def __init__(self, make, model, year):
        self.make = make
        self._model = model
        self.year = year

    def display_info(self):
         print(f"Car Details: {self.year} {self.make} {self.model}")

    def __update_model(self, new_model):
        self._model = new_model

    def __str__(self):
        return f"Car(Make: {self.make}, Model: {self._model}, Year: {self.year})"

