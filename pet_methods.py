class Pet:
    def __init__(self, name, category, account_balance, age = 0,):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False
        self.account_balance = 0
    
    def __str__(self):
        # States all information of the pet
        my_status = f'Name: {self.name} \n Category: {self.category} \n Age: {str(self.age)} \n Vaccination Status: {self.vaccinated} \n Account Balance: {self.account_balance} '
        return my_status
    
    # This method adds one to the age of the pet
    def have_birthday(self):
        self.age += 1
    
    # This methods changes the vaccinated value to True
    def vaccinate(self):
        self.vaccinated = True

# This method changes the account_balance and resets it to zero value
    def clear_balance(self):
        self.account_balance = 0
    
    # This method changes the age of the pet depending if the pet is a dog or a cat
    def age_and_category(self):
        if self.category == 'Dog':
            self.age *= 7
        elif self.category == "Cat":
            self.age = 6

p1 = Pet('Bonnie', 'Cat', age = 10, account_balance = 90)

# Calls all methods then prints pets attributes
p1.have_birthday()
p1.vaccinate()
p1.clear_balance()
p1.age_and_category()
print(p1)