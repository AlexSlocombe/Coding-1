import random

class dice:
    def __init__(self, sides, numRolls, numDice):
        self.sides = sides
        self.numRolls = numRolls
        self.numDice = numDice
    
    def rollDice(self):
        sides = int(input("How many sides on the dice: "))
        numRolls = int(input("How many rolls: "))
        numDice = int(input("How many dice: "))

        for i in range(0, numRolls):
            for x in range(0, numDice):
                print(random.randint(1, sides))

dice.rollDice(dice)