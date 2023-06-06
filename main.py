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


class ElectricScooter(Transport):
    __speed = 10
    __max_capacity = 4

    @property
    def speed(self):
        return self.__speed

    @property
    def max_capacity(self):
        return self.__max_capacity


class Bicycle(Transport):
    __speed = 15
    __max_capacity = 5

    @property
    def speed(self):
        return self.__speed

    @property
    def max_capacity(self):
        return self.__max_capacity


class Car(Transport):
    __speed = 40
    __max_capacity = 20

    @property
    def speed(self):
        return self.__speed

    @property
    def max_capacity(self):
        return self.__max_capacity


class Logistics(ABC):
    @abstractmethod
    def delivery_electric_scooter(self):
        raise NotImplementedError

    @abstractmethod
    def delivery_bicycle(self):
        raise NotImplementedError

    @abstractmethod
    def delivery_car(self):
        raise NotImplementedError


class OrderLogistic(Logistics):

    def __init__(self):
        self.__electric_scooter = ElectricScooter()
        self.__bicycle = Bicycle()
        self.__car = Car()

    def delivery_electric_scooter(self):
        print(f"Доставка еды электро самокатом, скорость {self.__electric_scooter.speed}, "
              f"вместимость {self.__electric_scooter.max_capacity}")

    def delivery_bicycle(self):
        print(f"Доставка еды велосипедом, скорость {self.__bicycle.speed}, вместимость {self.__bicycle.max_capacity}")

    def delivery_car(self):
        print(f"Доставка еды автомобилем, скорость {self.__car.speed}, вместимость {self.__car.max_capacity}")


def execute_application():
    logistic = OrderLogistic()
    logistic.delivery_electric_scooter()
    logistic.delivery_bicycle()
    logistic.delivery_car()


if __name__ == "__main__":
    execute_application()
