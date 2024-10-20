from abc import ABC, abstractmethod


class Vehicle(ABC):

    vehicle_count = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Vehicle.vehicle_count += 1

    @abstractmethod
    def max_speed(self):
        pass

    def display_info(self):
        print(f"Марка: {self.__brand}, Модель: {self.__model}")

    @classmethod
    def get_vehicle_count(cls):
        return cls.vehicle_count


class Car(Vehicle):
    def __init__(self, brand, model, horsepower):
        super().__init__(brand, model)
        self.__horsepower = horsepower

    def max_speed(self):

        return self.__horsepower * 0.5

    def display_info(self):
        super().display_info()
        print(f"Мощность: {self.__horsepower} л.с., "
              f"Максимальная скорость: {self.max_speed()} км/ч")


class Bike(Vehicle):
    def __init__(self, brand, model, weight):
        super().__init__(brand, model)
        self.__weight = weight  

    def max_speed(self):

        return max(self.__weight * 0.5, 30)

    def display_info(self):
        super().display_info()
        print(f"Вес: {self.__weight} кг, "
              f"Максимальная скорость: {self.max_speed()} км/ч")


if __name__ == "__main__":
    car1 = Car("Toyota", "Corolla", 130)
    bike1 = Bike("Yamaha", "YZF-R3", 160)

    car1.display_info()
    bike1.display_info()

    print(f"Общее количество транспортных средств: {Vehicle.get_vehicle_count()}")
