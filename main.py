from abc import ABC, abstractmethod


# Задание 1.
# Реализуйте архитектуру приложения, используя паттерн «Фабричный
# метод».
# Представьте, что вы создали программу управления доставкой еды. В
# программе в качестве единственного средства доставки используется электросамокат.
# Ваши курьеры на электро-самокатах развозят еду из пункта А в
# пункт Б. Все просто.
# Программа набирает популярность и ваш бизнес растет. Парк самокатов
# ограничен и вы решаете подключить к вашей системе доставки велосипеды и
# автомобили. Вам важно знать когда будет доставлена еда и сколько единиц
# продуктов может забрать курьер. У транспортных средств разная скорость и
# вместимость.

class Transport(ABC):
    __speed = None
    __max_capacity = None

    @abstractmethod
    def speed(self):
        raise NotImplementedError

    @abstractmethod
    def max_capacity(self):
        raise NotImplementedError

    @abstractmethod
    def deliver(self):
        raise NotImplementedError


class ElectricScooter(Transport):
    __speed = 10
    __max_capacity = 4

    @property
    def speed(self):
        return self.__speed

    @property
    def max_capacity(self):
        return self.__max_capacity

    def deliver(self):
        print(
            f"Доставка еды транспортом типа ElectricScooter, скорость - {self.__speed}, вместимость - {self.__max_capacity}")


class Bicycle(Transport):
    __speed = 15
    __max_capacity = 5

    @property
    def speed(self):
        return self.__speed

    @property
    def max_capacity(self):
        return self.__max_capacity

    def deliver(self):
        print(f"Доставка еды транспортом типа Bicycle, скорость - {self.__speed}, вместимость - {self.__max_capacity}")


class Car(Transport):
    __speed = 40
    __max_capacity = 20

    @property
    def speed(self):
        return self.__speed

    @property
    def max_capacity(self):
        return self.__max_capacity

    def deliver(self):
        print(f"Доставка еды транспортом типа Car, скорость - {self.__speed}, вместимость - {self.__max_capacity}")


class Logistics(ABC):
    @abstractmethod
    def create_transport(self):
        raise NotImplementedError


class ScooterLogistic(Logistics):
    def create_transport(self):
        return ElectricScooter()


class BicycleLogistic(Logistics):
    def create_transport(self):
        return Bicycle()


class CarLogistic(Logistics):
    def create_transport(self):
        return Car()


def execute_application():
    scooter_log = ScooterLogistic()
    scooter = scooter_log.create_transport()
    scooter.deliver()

    bicycle_log = BicycleLogistic()
    bicycle = bicycle_log.create_transport()
    bicycle.deliver()

    car_log = CarLogistic()
    car = car_log.create_transport()
    car.deliver()


if __name__ == "__main__":
    execute_application()
