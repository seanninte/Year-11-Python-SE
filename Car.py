class Car:
    def __init__(self, category, colour, wheels = 4, price):
        self.category = category
        self.colour = colour
        self.wheels = wheels
        self.price = price
    # States all properties of each car
    def __str__(self):
        car_properties = f'Category: {self.category} \n Colour: {self.colour} \n Wheels: {str(self.wheels)} \n Seats: {self.seats} \n Price: {self.price}'
        return car_properties

# Different variations of cars and their properties
c1 = Car('Ferrari', 'Red', '4', '$1,000,000')
c2 = Car('Toyota', 'White', '4', '$10,000')
c3 = Car('Acura NSX', 'Black', '4', '$100,000')

# Put into a list
cars = [c1, c2, c3]

# Prints each car and their properties
for i in cars:
    print(cars)
    print("")
