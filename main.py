from abc import ABC, abstractmethod


# Задание 2.
# Реализуйте архитектуру приложения, используя паттерн «Строитель».
# Чтобы построить стандартный дом, нужно поставить 4 стены,
# установить двери, вставить пару окон и постелить крышу. Но что, если вы
# хотите дом побольше, посветлее, с бассейном, садом и прочим добром?
# Паттерн предлагает разбить процесс конструирования объекта на
# отдельные шаги (например, построить стены, вставить двери и т.д.) Чтобы
# создать объект, вам нужно поочерёдно вызывать методы строителя. Причём
# не нужно запускать все шаги, а только те, что нужны для производства
# объекта определённой конфигурации

class Wall(ABC):
    pass


class BrickWall(Wall):
    def __str__(self):
        return "кирпич"


class Door(ABC):
    pass


class WoodenDoor(Door):
    def __str__(self):
        return "деревянная дверь"


class Window(ABC):
    pass


class PlasticWindow(Window):
    def __str__(self):
        return "пластиковые окна"


class Roof(ABC):
    pass


class FlexibleRoofTiles(Roof):
    def __str__(self):
        return "гибкая черепица"


class Pool:
    def __init__(self, width: float, length: float):
        self.width = width
        self.length = length


class Garden:
    def __init__(self, width: float, length: float):
        self.width = width
        self.length = length


class Builder(ABC):

    @abstractmethod
    def create(self):
        raise NotImplementedError

    @abstractmethod
    def build_walls(self, wall):
        raise NotImplementedError

    @abstractmethod
    def install_doors(self, door, count: int):
        raise NotImplementedError

    @abstractmethod
    def insert_window(self, window, count_window: int):
        raise NotImplementedError

    @abstractmethod
    def build_roof(self, value: int):
        raise NotImplementedError

    @abstractmethod
    def build_pool(self, pool: Pool):
        raise NotImplementedError

    @abstractmethod
    def get_house(self):
        raise NotImplementedError


class House:
    def __init__(self):
        self.walls = None
        self.doors = None
        self.window = None
        self.roof = None
        self.pool = None
        self.garden = None


class BuilderHouse(Builder):
    __house: House

    def create(self):
        self.__house = House()
        print("Начало постройки дома.")

    def build_walls(self, wall):
        self.__house.walls = BrickWall()
        print(f"Построили стены. Материал: {self.__house.walls}")

    def install_doors(self, door, count_doors: int):
        self.__house.doors = WoodenDoor()
        print(f"Установили двери. Материал: {self.__house.doors}, в количестве {count_doors} штук.")

    def insert_window(self, window, count_window: int):
        self.__house.window = PlasticWindow()
        print(f"Установили окна. Материал: {self.__house.window}, в количестве {count_window} штук.")

    def build_roof(self, roof):
        self.__house.roof = FlexibleRoofTiles()
        print(f"Установили крышу. Материал: {self.__house.roof}.")

    def build_pool(self, poll: Pool):
        self.__house.pool = poll
        print(f"Построили бассейн. Размер: {poll.width}x{poll.length}.")

    def get_house(self):
        print("Дом готов к эксплуатации.")
        return self.__house


def execute_application():
    builder_house = BuilderHouse()
    builder_house.create()
    builder_house.build_walls(BrickWall())
    builder_house.install_doors(WoodenDoor, 5)
    builder_house.insert_window(PlasticWindow(), 8)
    builder_house.build_roof(FlexibleRoofTiles())
    builder_house.build_pool(Pool(5, 4))
    builder_house.get_house()


if __name__ == "__main__":
    execute_application()
