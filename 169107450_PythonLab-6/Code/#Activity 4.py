#Activity 4: The __str__ Method
#Implement the __str__ method to define a string representation for the #Car class instances.
class Car:
  # Existing methods and __init__
     def __init__(self, make, model, year):
        self.make = make
        self.__model = model    
        self.year = year

def display_info(self):
        print(f"Car Details: {self.year} {self.make} {self.__model}")

def __update_model(self, new_model):
        self.__model = new_model

def update_model(self, new_model):
        self.__update_model(new_model)
        print(f"Model updated to: {new_model}")
# Your code here to return a string representation    
def __str__(self):
        return f"{self.year} {self.make} {self.__model}"
       


