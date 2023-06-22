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
class PasswordError(Exception):
    def __init__(self, text: str):
        self.text = text


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

    def __init__(self, door: Door):
        self.__door = door

    @staticmethod
    def set_password(password: str):
        SecurityDoor.__password = password
        print(f"Новый пароль {SecurityDoor.__password}.")

    def __authentication(self, password: str):
        return password == self.__password

    def open(self, password_input: str):
        if not self.__authentication(password_input):
            raise PasswordError(f"Не верный пароль. Дверь закрыта.")
        self.__door.open()

    def close(self):
        self.__door.close()


def execute_application():
    laboratory_door = LaboratoryDoor()
    security_door = SecurityDoor(laboratory_door)
    security_door.set_password("123")
    try:
        security_door.open("123")
        security_door.close()
    except PasswordError as e:
        print(e)


if __name__ == "__main__":
    execute_application()
