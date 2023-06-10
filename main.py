from abc import ABC, abstractmethod


# Задание 1.
# Паттерн «Заместитель».
# Представьте себе дверь, которую можно открыть лишь картой доступа
# либо нажатием кнопки. Главная функциональность двери — это ее открытие,
# а заместитель, который добавлен поверх (кнопка, карт-ридер), отвечает за
# безопасность и расширяет функциональность.
# Создайте абстрактный класс Door с методами open() и close().
# Реализуйте наследника этого класса LaboratoryDoor, который реализует
# методы этого класса.
# Также у нас будет существовать заместитель Security, обеспечивающий
# защиту любых дверей.
# Реализуйте класс заместитель SecurityDoor, который в конструкторе
# принимает объект класса Door. Класс заместителя должен реализовывать те
# же методы, что и наследники класса Door. В методе open() необходимо
# выполнить аутентификацию. Аутентификацию реализовать отдельным
# методом, который принимает пароль и определяет, подходит он к двери или
# нет. Таким образом к оригинальной двери мы накладываем логику проверки
# доступа.
class Door(ABC):
    @abstractmethod
    def open(self):
        raise NotImplementedError

    @abstractmethod
    def close(self):
        raise NotImplementedError


class LaboratoryDoor(Door):
    def open(self):
        print("Дверь открыта.")

    def close(self):
        print("Дверь закрыта.")


class SecurityDoor:
    __password = "12345"

    def __init__(self, input_password: str, door: LaboratoryDoor):
        self.__input_password = input_password
        self.__door = door

    def __is_valid_password(self):
        return self.__input_password == SecurityDoor.__password

    def open(self):
        print("Верный пароль, дверь открыта.") if self.__is_valid_password() else print("Не верный пароль.")

    @staticmethod
    def close():
        print("Дверь закрыта.")


def execute_application():
    laboratory_door = LaboratoryDoor()
    security_door = SecurityDoor("12345", laboratory_door)
    security_door.open()
    security_door.close()


if __name__ == "__main__":
    execute_application()
