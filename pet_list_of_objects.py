class Pet:
    def __init__(self, name, category, age = 0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False

    def __str__(self):
        # States all information of the pet
        my_status = f'Name: {self.name} \n Category: {self.category} \n Age: {str(self.age)} \n Vaccination Status: {self.vaccinated}'
        return my_status

# Defines pet and their name, category and age
p1 = Pet('Bonnie', 'Cat')
p2 = Pet('Clyde', 'Dog', 7)
p3 = Pet(category = 'Rabbit', name = 'Ruby', age = 13)
p4 = Pet(name = 'John', category = 'Cat', age = 3)

# Puts all pets into a list and adds Pet 4 to list
pets = [p1, p2, p3]
pets.append(p4)

# Changes every vaccination status to True using for loop
# Prints all pets information
for pet in pets:
    pet.vaccinated = True
    print(pet)
    print("")
