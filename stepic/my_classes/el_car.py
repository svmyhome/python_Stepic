from my_car import Car
import battery_car


class ElectricCar(Car):
    """Docs"""

    def __init__(self, year, model, name, distance=0):
        super().__init__(year, model, name)
        self.capacity1 = battery_car.Battery(400)
        self.distance = distance

    def print_information(self):
        model_info = f"{self.name} {self.model} {self.year} {self.distance} {self.capacity1.capacity} {self.capacity1.count_recicle}"
        return model_info.title()
