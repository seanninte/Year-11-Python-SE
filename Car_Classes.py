class Car:
    def __init__(self,make,model,year,price=None, for_sale = True):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.for_sale = for_sale

    def __str__(self):
        # States alls properties and status of the cars
        status = f'Make: {self.make} \n Model: {self.model} \n Year: {str(self.year)} \n Price: {self.price} \n Sale Status: {self.for_sale}'
        return status
        sale_status = True 

# Puts cars into list
c1 = Car('Mazda','6', 2005)
c2 = Car('Honda Acura NSX', '2', 2016)
c3 = Car('EK Civic', '5', 2002)
c4 = Car('BMW', '8', 2019)
cars = [c1, c2, c3]

# Prints all cars and their status and features in a for loop
for car in cars:
    print(car)
    print("")

