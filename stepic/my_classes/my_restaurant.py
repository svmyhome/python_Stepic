class Restaurant():
    def __init__(self, name, open, closed):
        self.name = name
        self.open = open
        self.closed = closed
        self.visitors = 0

    def names(self):
        print(self.name)

    def works(self):
        print(self.open)
        print(self.closed)

    def return_visitors(self):
        return self.visitors

    def set_visitors(self, count):
        self.visitors = count

    def update_visitors(self, count):
        self.visitors += count


class Cafe(Restaurant):

    def __init__(self, name, open, closed):
        super().__init__(name, open, closed)
        self.kind_ice = ['Vanil', 'banana']



new_res = Restaurant("kdmcksd", 12, 12)
new_res.names()
new_res.works()
print(new_res.visitors)
new_res.visitors = 1
print(new_res.visitors)
new_res.set_visitors(12)
print(new_res.visitors)
new_res.update_visitors(1111)
print(new_res.visitors)

ice = Cafe('cjdn', 12, 12)
print(ice.kind_ice, ice.name)