# 76009632
class Stack:
    # Создаем список примежуточных результатов (СПР).
    def __init__(self):
        self.result = []
    
    # Метод добавляет числа в СПР.
    def push(self, value):
        self.result.append(value)
    
    # Метод производит арифметическую операцию исходя из входящего знака.
    def action(self, sign):
        # "Отрезаем" последний элемент СПР, второй по порядку вхождения в СПР.
        second = self.result.pop()
        # Еще раз "отрезаем" эл-т. Он первый по порядку вхождения в СПР.
        first = self.result.pop()
        # Производим операцию с подготовленными эл-ми СПР исходя из знака на входе.
        if sign == '*':
            self.result.append(first * second)
        elif sign == '/':
            self.result.append(first // second)
        elif sign == '+':
            self.result.append(first + second)
        elif sign == '-':
            self.result.append(first - second)
    
    # Метод возвращает промежуточный/конечный результат из СПР.
    def return_result(self):
        return self.result[-1]

# Функция для расчета результата входящего выражения.
def calculation(data):
    stack = Stack()
    # Заранее определяем список знаков.
    list_sign = '*/+-'
    for value in data:
        # Проверяем является ли элемент знаком.
        if value in list_sign:
            # Если да, то производим мат. операцию.
            stack.action(value)
        else:
            # Иначе, просто добавляем в СПР.
            stack.push(int(value))
    # После перебора всех элементов входящего выражения, выводим результат.
    return stack.return_result()
        

def read_input():
    return input().strip().split()

def main():
    # Считываем входящие данные.
    data = read_input()
    # Печатаем получившийся результат.
    print(calculation(data))

if __name__ == '__main__':
    main()
