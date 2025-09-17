import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.health = starting_health
        self.weapon = weapon
        self.shield = shield

    def report(self):
        print(self.name + ' Health: '+ str(self.health))

    def move(self):
        print("What will you do?") # Provides player various options of moves during their turn
        print("(1) Attack | (2) Skill")
        print("(3) Defend | (4) Heal")

    def is_dead(self):
        if self.health <= 0:
            return True
        else:
            return False

    def random_attack(self):
        attack_power = random.randint(self.weapon/2, self.weapon*2)
        print('Attack Damage:', attack_power)
        return attack_power

    def skill_attack(self): # skill_attack method similar to random_attack but user must correctly time input to wither increase or decrease value of attack
        attack_power = random.randint(self.weapon/2, self.weapon*2)
        target = random.randint(2,6) # Uses random module to randomise the target time to input multiplier attack
        print('Hit enter in exactly',target,'seconds')
        tic = time.time() # tic and toc variables to measure time taken for input
        input()
        toc = time.time()
        time_taken = toc - tic
        multiplier = 3 - abs(target-time_taken)
        if multiplier < 2: 
            multiplier = 0
        print('Skill Attack Power:', attack_power)
        print('Multiplier:', multiplier)
        return attack_power*multiplier

    def defend(self,attack_power):
        damage = attack_power - self.shield
        if damage >  0:
            self.health -= damage
            print('Damage:', damage)
        else:
            print('No damage')

    def defend_move(self, attack_power): # Similar to defend, reduces the incoming attack by 50%
        damage = attack_power - self.shield
        self.health = self.health - damage/2
        print("Defended Attack, Reduced by 50%")
    
    def heal_move(self, healing): # Adds 100 to players health attribute
        self.health = self.health + 100
        print("You were healed.")
        print("Health:", self.health)

class Monster(Fighter): # Subclass of Fighter for enemy opponent
    def __init__(self,name, starting_health, weapon, shield, strength = 70):
        super().__init__(name, starting_health, weapon, shield)
        self.strength = strength # Monsters exclusive attribute strength, addition damage to attack

    def random_attack(self): # Randomly create value of attack
        attack_power = random.randint(self.weapon/2, self.weapon*2) # Randomly selects if attack is weaker or stronger
        print('Attack Damage:', attack_power)
        return attack_power + self.strength
    



# Characters and their attribute values for health, weapon damage and shield
you = Fighter('You',300,60,20)
monster = Monster('Monster',300,40,30)

# Provides player context of game's story
print('')
print('You wake up in a forest filled with dangerous monsters . . .')
time.sleep(2)
print('You see a mysterious figure approach you . . .')
time.sleep(2)
print('')
you.report()
monster.report()
print('')
print("Your battle begins . . .")
print('')

while True: # While loop to simulate turn based attacks until one of the character reach zero health
    time.sleep(3)
    you.move()
    user_move = input("Your move: ") # Asks player for their move
    print('')
    if user_move == '1': # Activates random_attack method 
        print("You attacked the enemy.")
        monster.defend(you.random_attack)
        you.report()
        monster.report()    
        time.sleep(1)
        print()
        print("The enemy attack you . . .")
        you.defend(monster.random_attack)
        you.report()
        monster.report()
        print('')
        time.sleep(1)
    elif user_move == "2": # Activates skill_attack method
        monster.defend(you.skill_attack)
        you.report()
        monster.report()
        time.sleep(1)
        print()
        print("The enemy attacks you . . .")
        you.defend(monster.random_attack)
        you.report()
        monster.report()
        print('')
        time.sleep(1)
    elif user_move == "3": # Activates defend_move method
        print("You are defending")
        print("The enemy attacks you . . .")
        you.defend_move(monster.random_attack)
        time.sleep(1)
        print()
        you.report()
        monster.report()
        print('')
    elif user_move == "4": # Activates heal_move method
        you.heal_move(monster.random_attack)
        print('')
        time.sleep(1)
        print("The enemy attacks you . . .")
        you.defend(monster.random_attack)
        time.sleep(1)
        you.report()
        monster.report()
        print('')
    if monster.is_dead(): # Ends battle simulation if player or enemy monster is_dead is equal to True
        you.defend(monster)
        print("You have won the battle.")
        break
    if you.is_dead():
        print("You were slain.")
        print("GAME OVER")
        break