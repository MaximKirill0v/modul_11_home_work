from abc import ABC, abstractmethod


# Задание 1.
# Стратегия – это поведенческий паттерн проектирования, который
# определяет семейство схожих алгоритмов и помещает каждый из них в
# собственный класс, после чего алгоритмы можно взаимозаменять прямо во
# время исполнения программы.
# Вы решили написать приложение-навигатор для путешественников.
# Оно должно показывать красивую и удобную карту, позволяющую с лёгкостью
# ориентироваться в незнакомом городе.
# Одной из самых востребованных функций являлся поиск и
# прокладывание маршрутов. Пребывая в неизвестном ему городе, пользователь
# должен иметь возможность указать начальную точку и пункт назначения, а
# навигатор – проложит оптимальный путь.
# В этом примере каждый алгоритм поиска пути переедет в свой
# собственный класс. В этих классах будет определён лишь один метод,
# принимающий в параметрах координаты начала и конца пути, а
# возвращающий массив точек маршрута. Реализуйте класс навигатора,
# который по переданной ему стратегии выполняет построение маршрута.

class Point:
    def __init__(self, point_x: int, point_y: int):
        self.__point_x = point_x
        self.__point_y = point_y

    def __str__(self):
        return f"{self.__point_x, self.__point_y}"


class BaseStrategy(ABC):
    @abstractmethod
    def build_route(self, start_point: Point, finish_point: Point):
        raise NotImplementedError


class CarStrategy(BaseStrategy):
    def build_route(self, start_point: Point, finish_point: Point):
        return f"Маршрут построен из точки {start_point} в точку {finish_point}. Вид транспорта: автомобиль."


class PublicTransportStrategy(BaseStrategy):
    def build_route(self, start_point: Point, finish_point: Point):
        return f"Маршрут построен из точки {start_point} в точку {finish_point}. Вид транспорта: городской транспорт."


class WalkingStrategy(BaseStrategy):
    def build_route(self, start_point: Point, finish_point: Point):
        return f"Маршрут построен из точки {start_point} в точку {finish_point}. Вид транспорта: пешком."


class Navigator:
    __strategy = BaseStrategy

    def set_strategy(self, strategy: BaseStrategy):
        self.__strategy = strategy

    def build_route(self, start_point: Point, finish_point: Point):
        return self.__strategy.build_route(start_point, finish_point)


def execute_application():
    start_point = Point(0, 0)
    finish_point = Point(10, 10)
    navigator = Navigator()
    navigator.set_strategy(CarStrategy())
    print(navigator.build_route(start_point, finish_point))

    navigator.set_strategy(WalkingStrategy())
    print(navigator.build_route(start_point, finish_point))

    navigator.set_strategy(PublicTransportStrategy())
    print(navigator.build_route(start_point, finish_point))


if __name__ == "__main__":
    execute_application()
