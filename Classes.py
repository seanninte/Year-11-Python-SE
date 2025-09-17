class Pet:
    def __init__(self, name, category, age, vaccinated, ccard, billing_address):
        self.name = name # Defines value of all variables in the class
        self.category = category
        self.age = age
        self.vaccinated = vaccinated
        self.ccard = ccard
        self.billing_address = billing_address
        self.owner_name = 'unknown'
        self.account_balance = 0



# Pet's name, category, age, vaccination status, credit card and billing address
p1 = Pet('Bonnie','Cat', 3, True,'4566 0887 5678 7896', 'China')
p2 = Pet('Foxy', 'Dog', 4, False, '7890 4563 2234 5446', 'Australia')

print(f'{p1.name} vaccination status is {p1.vaccinated}.') # Prints vaccination status of p1 and p2
