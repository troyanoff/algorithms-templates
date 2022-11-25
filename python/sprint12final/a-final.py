# 76203568
class Deque:
    """Класс для реализации очереди типа дек."""

    def __init__(self, n):
        # Для реализации логики сразу создаем список заданной длинны.
        self.__deque = [None] * n
        # Запоминаем максимальную длинну очереди
        self.__max_n = n
        # Определяем индекс начала списка, "головы".
        self.__head = 0
        # Определяем индекс первого пустого эл-та с конца, "хвост".
        self.__tail = 0
        # Определяем размер заполненной очереди.
        self.__size = 0

    def __offset_index(self, index, offset):
        """Метод для смещения индекса."""
        # Проверяем куда нужно сместить индекс.
        if offset == 'forward':
            index = (index + 1) % self.__max_n
        # По идее, лишнее обращение к переменной, поэтому esle на доверии.
        else:
            index = (index - 1 + self.__max_n) % self.__max_n
        return index

    def is_empty(self):
        """Метод проверяет, пуста ли очередь."""
        return self.__size == 0

    def is_full(self):
        """Метод проверяет, заполнена ли очередь."""
        return self.__size == self.__max_n

    def push_back(self, value):
        """Метод добавляет значение в конец очереди."""
        # Проверяем не забита ли очередь.
        if self.is_full():
            return 'error'
        # Помещаем входящее значение в конец 
        self.__deque[self.__tail] = value
        # Смещаем индекс первой пустой ячейки.
        self.__tail = self.__offset_index(self.__tail, 'forward')
        # Увеличиваем размер очереди.
        self.__size += 1

    def push_front(self, value):
        """Метод добавляет значение в начало очереди."""
        # Проверяем не забита ли очередь.
        if self.is_full():
            return 'error'
        # Сразу смещаем индекс первого эл-та в очереди.
        self.__head = self.__offset_index(self.__head, 'back')
        # Добавляем в него входящее значение.
        self.__deque[self.__head] = value
        # Увеличиваем размер очереди.
        self.__size += 1

    def pop_back(self):
        """Удаляем последний элемент очереди."""
        # Для начала проверяем не пуста ли очередь.
        if self.is_empty():
            return 'error'
        # Смещаем индекс хвоста на -1.
        # Теперь он указывает на последнее значение.
        self.__tail = self.__offset_index(self.__tail, 'back')
        # Запоминаем это значение для вывода.
        pop_value = self.__deque[self.__tail]
        # Удаляем это значение из очереди.
        self.__deque[self.__tail] = None
        # Уменьшаем размер очереди.
        self.__size -= 1
        return pop_value

    def pop_front(self):
        """Удаляем первый элемент очереди."""
        # Для начала проверяем не пуста ли очередь.
        if self.is_empty():
            return 'error'
         # Запоминаем значение для вывода.
        pop_value = self.__deque[self.__head]
        # Удаляем это значение из очереди.
        self.__deque[self.__head] = None
        # Смещаем индекс головы на первый элемент в очереди.
        self.__head = self.__offset_index(self.__head, 'forward')
        # Уменьшаем размер очереди.
        self.__size -= 1
        return pop_value

def deque_process(max_size, commands):
    """Функция для работы с дек-очередью.
    
    Функция принимает на вход максимальную длинну и список команд 
    для работы с очередью типа дек через класс Deque:
    создание экземпляра класса с последующей обработкой команд
    и вывода промежуточных результатов.
    """
    # Создаем экземпляр дека той длинны, которая передана на вход.
    deque = Deque(n = max_size)
    # Определяем команды для добавления элеметнов.
    push_commands = ['push_back', 'push_front']
    # Далее проходим по списку команд, выполняя их.
    for command, *value in commands:
        # Проверку на полную очередь c выводом ошибки.
        if ((command in push_commands) and deque.is_full()):
            print('error')
        # Если команда на добавление, то передаем значение.
        elif command in push_commands:
            getattr(deque, command)(int(value[0]))
        else:
            print(getattr(deque, command)())

def read_input():
    """Функция считывания данных для дек-очереди.
    
    Функция для считывания числа команд, максимального размера очереди
    и самих команд, формируя общий список команд, удобный для обработки.
    Выводит максимальную длинну очереди и список команд.
    """
    count_commands = int(input())
    max_size = int(input())
    commands = []
    # Считываем заданное количество комманд,
    # Добавляя их в общий список на вывод.
    for _ in range(count_commands):
        commands.append(input().strip().split())
    return max_size, commands

def main():
    max_size, commands = read_input()
    deque_process(max_size, commands)

if __name__ == '__main__':
    main()

