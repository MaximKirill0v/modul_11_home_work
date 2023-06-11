from math import sqrt
from datetime import datetime
import time
import datetime


# Задание 1.
# Создайте функцию, возвращающую список со всеми простыми числами
# от 0 до 1000. Используя механизм декораторов посчитайте сколько секунд,
# потребовалось для вычисления всех простых чисел. Отобразите на экран
# количество секунд и простые числа
# Задание 2.
# Добавьте к первому заданию возможность передавать границы
# диапазона для поиска всех простых чисел
# Задание 3.
# Создайте функцию для отображения текущего времени. Функция не
# принимает параметров.
# Задание 4.
# Используя синтаксис декораторов, произведите декорирование
# функции из задания 3. Потенциальный вывод данных на экран после
# декорирования:
# ***************************
# 23:00
# ***************************
def get_time_work_func(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        res_list = func(*args, **kwargs)
        end = datetime.now()
        return f"{res_list}\n" \
               f"Время выполнения функции: {end - start}с."

    return wrapper


@get_time_work_func
def get_simple_digit_list(min_range: int = 2, max_range: int = 1001):
    res_list = []
    for digit in range(min_range, max_range):
        for num in range(2, int(sqrt(digit) + 1)):
            if digit % num == 0:
                break
        else:
            res_list.append(digit)
    return res_list


def get_symbol(symbol: str = '*', number_symbol: int = 20):
    def output_with_symbols(func):
        def wrapper(*args, **kwargs):
            time_now = func()
            return f"{symbol * number_symbol}\n{time_now}\n{symbol * number_symbol}"

        return wrapper

    return output_with_symbols


@get_symbol('=', 30)
def get_time_now():
    return datetime.datetime.now().strftime('%H:%M')


def execute_application():
    # Задание 1 и 2
    # simple_digit_list_with_time = get_simple_digit_list(10, 100000)
    # print(simple_digit_list_with_time)

    # Задание 3 и 4
    # time_now = get_time_now()
    # print(f"{time_now}")


if __name__ == "__main__":
    execute_application()
