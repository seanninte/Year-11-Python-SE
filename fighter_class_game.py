import random

class Fighter: # Creates class of the character and its attribute with a private health attribute
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health
        self.weapon = weapon
        self.shield = shield

    def report(self): # Prints out the character name and health after each turn of attack
        print(self.name + ' Health: ' + str(self.__health))
    
    def get_health(self): # Able to get private attribute health 
        return self.__health
    
    def random_attack(self): # Randomly create value of attack
        attack_power = random.randint(self.weapon/2, self.weapon*2)
        print('Damage:', attack_power)
        return attack_power

# Characters and their attribute values for health, weapon damage and shield
you = Fighter('You', 100, 60, 20)
troll = Fighter('Troll', 200, 30, 10)

# Variables that gather the private attribute health
you_health = you.get_health()
troll_health = troll.get_health()

# While loop to simulate turn based attacks until one of the character reach zero health
while you_health > 0 or troll_health > 0:
    print()
    print('You attacked the troll.')
    troll_health -= you.random_attack() # Minuses the health of the troll to the attack value
    print('Troll health:',troll_health)
    print()
    if troll_health < 0: # If the health of the troll is less than zero, game ends and user wins
        print()
        print('You win the battle.')
        break
    elif you_health < 0: # If the health of the user is less than zero, game ends and troll wins
        print()
        print('You lost the battle.')
        print('GAME OVER')
        break
    print("Troll attacked you")
    you_health -= troll.random_attack()
    print('Your health:',you_health)