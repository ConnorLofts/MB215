#Activity 3: Hiding Data Attributes
#Modify the Car class to make the model attribute private. This should #prevent it from being accessed directly from an instance.

class Car:
    # Modify the __init__ method to make model private
    # Your updated code here
# car.py (updated)
    def __init__(self, make, model, year):
        self.make = make
        self._model = model 
        self.year = year

    def display_info(self):
        print(f"Car Details: {self.year} {self.make} {self.model}")

    def __update_model(self, new_model):
        self._model = new_model