import el_car
class Car():
    def __init__(self, year, model, name):
        self.year = year
        self.model = model
        self.name = name
        self.odometer = 100

    def print_information(self):
        model_info = f"{self.name} {self.model} {self.year} {self.odometer}"
        return model_info.title()

    def set_odo(self, value):
        if self.odometer <= value:
            self.odometer = value
        else:
            print('Less')

    def update_odo(self, value):
        self.odometer += value


my_new_car = Car(2021, 'lambo', 'huracane')
print(my_new_car.print_information())
my_new_car.odometer = 10
print(my_new_car.print_information())
my_new_car.set_odo(1)
print(my_new_car.print_information())
my_new_car.update_odo(10)
print(my_new_car.print_information())





tesla = el_car.ElectricCar(2022, 'X', "Tesla", 4)
print(tesla.print_information())
tesla.capacity1.status_battery()
print(tesla.capacity1.count_recicle)
print(tesla.capacity1.charge)