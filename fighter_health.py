import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health # Health becomes a private attribute because of the double underscore and cannot be accessed outside the class.
        self.weapon = weapon
        self.shield = shield

    def report(self):
        print(self.name+':'+ ' Health: '+ str(self.__health))

    def is_dead(self): # Method which checks private attribute health through if statement. if health is equal or less than  zero, method will return as True
        if self.__health <= 0:
            return True
        else:
            return False

    def random_attack(self):
        attack_power = random.randint(self.weapon/2, self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power

    def defend(self,attack_power):
        damage = attack_power - self.shield
        if damage >  0:
            self.__health -= damage
            print('Damage:', damage)
        else:
            print('No damage')


you = Fighter('You',100,60,20)
troll = Fighter('Troll',200,30,10)

you.report()
troll.report()
print()

while True: # While loop to simulate battle until one of the characters health reaches or is less than zero
    print('You attack the troll')
    troll.defend(you.random_attack()) # Generates attack by calling random_attack function
    troll.report()
    time.sleep(1) # Uses time module to delay text by one second
    print()
    if troll.is_dead(): # Battle ends once troll health reaches zero or lower
        print('You win')
        break
    print('The troll attacked you ')
    you.defend(troll.random_attack())
    you.report()
    time.sleep(1)
    if you.is_dead(): # Calls is_dead method to check if the health of the character is less than or equal to zero.
        print('The troll wins') # Prints outcome of battle
        break
    print()