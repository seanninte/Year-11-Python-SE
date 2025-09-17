name = 'Bonnie'
animal_category = 'Cat'
age = 3
vaccinated = True
ccard = '3423 2326 7543 1234'
billing_address = '17 Park Drive, The Shire 2695'
owner_name = 'Alex Ngyuen'
account_balance = 129.95

def help():
    print('Welcome to the Pet Data Management System')
    print("Every vet's best friend")

def increase_age():
    global age
    age = age + 1

# If the length of the credit card number is 19 characters and is split into 4, it will be deemed valid
def verify_credit_card(card_num):
    input("Verify credit card number: ")
    if len(card_num) == 19:
        if len(card_num.split()) == 4:
            return True
            print("Credit Card Number is Valid")
            # If the credit card number is valid, the account balance will have 39 less 
            account_balance - 39
    return False

# If the vaccinated value is equal to false, it will change it to True
def vaccinate()
    if vaccinated == False:
        vaccinated == True

help()
increase_age()
print(age)