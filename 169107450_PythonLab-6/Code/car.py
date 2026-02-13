class Car:
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

    def __str__(self):
        return f"{self.year} {self.make} {self.__model}"