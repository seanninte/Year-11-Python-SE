class Pet:
    def __init__(self, name, category, age = 0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False
    def __str__(self):
        # Identifies if the Credit Card is valid based on the length of the card number
        payment_status = 'Unregistered'
        if len(self.ccard) == 19:
            payment_status = 'Registered'
        
        # States all information of the pet
        my_status = f'Name: {self.name} \n Category: {self.category} \n Age: {str(self.age)} \n Payment Status: {payment_status} \n Vaccination Status: {self.vaccinated}'
        return my_status

p1 = Pet('Bonnie', 'Cat', 4)
print(p1)
