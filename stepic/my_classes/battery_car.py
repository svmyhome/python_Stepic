class Battery():
    def __init__(self, charge, capacity=25, count_recicle=11):
        self.capacity = capacity
        self.count_recicle = count_recicle
        self.charge = charge

    def status_battery(self):
        if self.capacity < 30 and self.count_recicle > 10:
            print(f'You power not enaught')
        else:
            print(f'Go GO GO')