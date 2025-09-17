class Pet:
    def __init__(self, name, category, breed = None, age = 0,):
        self._name = name
        self.__category = category
        self.__breed = breed
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False
        self.__weight = 0
    
    # Returns self weight value even in it is protected or private
    def get_weight(self):
        return self.__weight
    
    # Set function to input positive number for weight and changes the value to the new weight
    def set_weight(self, new_weight):
        if type(new_weight) == int or type(new_weight) == float:
            if new_weight > 0:
                self.__weight = new_weight
            else:
                print("Please enter a positive number.")
        else:
            print("Please enter a positive number.")

    def __str__(self):
        payment_status = 'unregistered'
        if len(self.__ccard) == 19:
            payment_status = 'registered'
        # States all information of pet
        my_status = 'Name: ' + self._name +'\nCategory: ' + self.__category + '\nAge: ' + str(self.age) +'\nPayment status: ' + payment_status + '\nVaccinated: '+ str(self.vaccinated) + '\nBreed: '+ str(self.__breed)
        return my_status

p1 = Pet(name = 'Bonnie', category = 'Cat', age = 10)
# Sets weight to new value and prints the function
p1.set_weight(12)
# Prints the set weight of the pet
print("Weight:", p1.__weight) 
print(p1)

