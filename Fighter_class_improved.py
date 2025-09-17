import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.health = starting_health
        self.weapon = weapon
        self.shield = shield

    def report(self): # Prints out the character name and health after each turn of attack
        print(self.name + ' Health: ' + str(self.health))
    
    def get_health(self): # Able to get private attribute health 
        return self.health
    
    def random_attack(self): # Randomly create value of attack
        attack_power = random.randint(self.weapon/2, self.weapon*2) # Uses random module to generate value of either a weaker attack or stronger attack
        print('Attack Damage:', attack_power)
        return attack_power
    
    def defend(self, attack_power): # Creates defend move which reduces value of the attack
        damage = attack_power - self.shield # Reduces value of attack by minus shield value
        if damage > 0:
            self.health = self.health - damage
            print('Defended Damage:', damage)
        else:
            print('No damage')


# Characters and their attribute values for health, weapon damage and shield
you = Fighter('You', 100, 60, 20)
troll = Fighter('Troll', 200, 30, 10)

you.report()
troll.report()
print()

while True: # While loop to simulate battle until one of the characters health reaches or is less than zero
    print('You attack the troll')
    troll.defend(you.random_attack()) # Generates attack by calling random_attack function
    troll.report()
    time.sleep(1) # Uses time module to delay text by one second
    print()
    if troll.health <= 0: # Battle ends once troll health reaches zero or lower
        print('You win')
        break
    print('The troll attacked you ')
    you.defend(troll.random_attack())
    you.report()
    time.sleep(1)
    if you.health <= 0:
        print('The troll wins')
        break
    print()