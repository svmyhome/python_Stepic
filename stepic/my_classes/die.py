from random import randint
class Die():

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

die1 = Die()
die1.roll_die()
die1.roll_die()
die1.roll_die()
die1.roll_die()
die1.roll_die()
die1.roll_die()
die1.roll_die()
print('------------')
die2 = Die(10)
die2.roll_die()
die2.roll_die()
die2.roll_die()
die2.roll_die()
die2.roll_die()
die2.roll_die()
die2.roll_die()