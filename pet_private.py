class Pet:
    def __init__(self, name, category, breed = None, age = 0):
        self._name = name # Uses single underscore to make attribute protected
        self.__category = category # Uses double underscore to make the attribute private
        self.__breed = breed
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False

    def have_birthday(self):
        self.age += 1

    def __str__(self):
        payment_status = 'unregistered'
        if len(self.__ccard) == 19:
            payment_status = 'registered'
        # States all information
        my_status = 'Name: ' + self._name +'\nCategory: ' + self.__category + '\nAge: ' + str(self.age) +'\nPayment status: ' + payment_status + '\nVaccinated: '+ str(self.vaccinated) + '\nBreed: '+ str(self.__breed)
        return my_status

p1 = Pet(name = 'Bonnie', category = 'Cat', age = 10)
print(p1)
# Attempts to print private category and breed and is unable to
print(p1.__category)
print(p1.__breed)