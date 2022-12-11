from random import choice
class Lot():

    def __init__(self):
        self.list_lot = ('a', 'b', 'c', 'd', 'e', 1, 2,3,4)

    def rand_ch(self):
        for _ in range(5):
            print(choice(self.list_lot))


lot1 = Lot()
lot1.rand_ch()