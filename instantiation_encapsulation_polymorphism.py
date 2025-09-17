#---begin Python ---
class Car:
    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.__year = year
        self.colour = colour
    
    def update_year(self):
        self.__year = self.__year + 1
        print(f"{self.__year}")

    def start(self):
        print(f"{self.make} {self.model} is starting.")

    def stop(self):
        print(f"{self.make} {self.model} is stopping.")



# Instantiating objects from the Car class
car1 = Car("Toyota", "Camry", 2020, "Red")
car2 = Car("Honda", "Civic", 2018, "Blue")
car3 = Car("Ford", "Mustang", "2021", "Black") 

car1.update_year()
print(car1)

#--- end python ---
