# 76384572
class StackIsEmpty(Exception):
    """Исключение для пустом стэке."""
    pass

class Stack:
    """Класс для реализации стэка."""

    def __init__(self):
        """Создаем список примежуточных результатов (СПР)."""
        self.__result = []

    def push(self, value):
        """Метод добавляет числа в СПР."""
        self.__result.append(value)

    def pop(self):
        """Метод возвращает промежуточный/конечный результат из СПР."""
        try:
            return self.__result.pop()
        except KeyError:
            raise StackIsEmpty('Стэк пуст.')

def calculation(data):
    """Функция для расчета результата входящего выражения."""
    stack = Stack()
    # Определяем лямбда-функции для каждого str-знака.
    operators = {
            '+': lambda first, second: first + second,
            '-': lambda first, second: first - second,
            '*': lambda first, second: first * second,
            '/': lambda first, second: first // second,
        }
    for value in data:
        # Проверяем является ли элемент знаком.
        if value in operators:
            # "Отрезаем" последний элемент СПР, второй по порядку вхождения в СПР.
            second = stack.pop()
            # Еще раз "отрезаем" эл-т. Он первый по порядку вхождения в СПР.
            first = stack.pop()
            # Если да, то производим мат. операцию.
            stack.push(operators[value](first, second))
        else:
            # Иначе, просто добавляем в СПР.
            stack.push(int(value))
    # После перебора всех элементов входящего выражения,
    # выводим последний эл-т стэка. По всей логике, это результат вычислений.
    return stack.pop()
        

def read_input():
    """Функция считывания данных."""
    return input().strip().split()

def main():
    # Считываем входящие данные.
    data = read_input()
    # Печатаем получившийся результат.
    print(calculation(data))

if __name__ == '__main__':
    main()
