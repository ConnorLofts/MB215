#Activity 2: Add Public and Private Methods
#Within the Car class, implement the following methods:

    # A public method display_info that prints the car's details.
    # A private method __update_model which changes the car's model.

class Car:
    # Existing __init__ method
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        # Your code here to print car details
        print(f"Car Details: {self.year} {self.make} {self.model}")
        pass
    def __update_model(self, new_model):
        self.__model = new_model

    
