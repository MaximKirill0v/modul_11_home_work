from abc import ABC, abstractmethod


# Задание 1.
# Реализуйте архитектуру приложения, используя паттерн
# «Абстрактная фабрика»
# Допустим, вы решили создать программу по производству и продаже
# автомобилей. Автомобили будем создавать сами. Лучшим решением будет
# скупить заводы известных компаний Ford и Toyota, и продолжить выпускать
# автомобили под их собственными марками, а прибыль класть себе в
# карман. Будем делать автомобили с 2 типами кузова – седан и купе. Например,
# японцы будут делать ToyotaSedan и ToyotaCoupe, американцы — FordSedan и
# FordCoupe». Таким образом, в вашем абстрактном классе CarsFactory будут 2
# метода: createSedan() и createCoupe(). Реализуйте программу и протестируйте
# фабрику на примерах создания конкретных автомобилей.

# Создать классы наследники от SedanCar ToyotaSedan и FordSedan.
# Создать классы наследники от CoupeCar ToyotaCoupe и FordCoupe.
# SedanCar и CoupeCar соответственно должны быть абстракциями и
# методы создающие автомобили уже не могу возвращать объект SedanCar
# и CoupeCar, а возвращают объекты классов наследников.
class CarBody(ABC):
    pass


class SedanCar(CarBody):
    pass


class CoupeCar(CarBody):
    pass


class ToyotaSedan(SedanCar):
    pass


class FordSedan(SedanCar):
    pass


class ToyotaCoupe(CoupeCar):
    pass


class FordCoupe(CoupeCar):
    pass


class CarFactory(ABC):
    @abstractmethod
    def create_sedan_car(self):
        raise NotImplementedError

    @abstractmethod
    def create_coupe_car(self):
        raise NotImplementedError


class ToyotaFactory(CarFactory):
    def create_sedan_car(self):
        print("Произведён автомобиль - ToyotaSedan")
        return ToyotaSedan

    def create_coupe_car(self):
        print("Произведён автомобиль - ToyotaCoupe")
        return ToyotaCoupe


class FordFactory(CarFactory):
    def create_sedan_car(self):
        print("Произведён автомобиль - FordSedan")
        return FordSedan

    def create_coupe_car(self):
        print("Произведён автомобиль - FordCoupe")
        return FordCoupe


def execute_application():
    toyota_factory = ToyotaFactory()
    toyota_factory.create_sedan_car()
    toyota_factory.create_coupe_car()

    ford_factory = FordFactory()
    ford_factory.create_sedan_car()
    ford_factory.create_coupe_car()


if __name__ == "__main__":
    execute_application()
