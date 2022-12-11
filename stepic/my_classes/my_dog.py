class Dog():
    """ First class """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def voice(self):
        print(f'The {self.name} is Gav')

    def rotate(self):
        print(f'The {self.name} have {self.age} and rotate')



my_dog1 = Dog('Arnold', 21)

my_dog1.voice()
my_dog1.rotate()
print(my_dog1.name)