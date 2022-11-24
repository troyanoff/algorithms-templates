# 75798714
class Deque:
    """Класс для реализации очереди типа дек."""
    def __init__(self, n):
        # Для реализации логики сразу создаем список заданной длинны.
        self.deque = [None] * n
        # Запоминаем максимальную длинну очереди
        self.max_n = n
        # Определяем индекс начала списка, "головы".
        self.head = 0
        # Определяем индекс первого пустого эл-та с конца, "хвост".
        self.tail = 0
        # Определяем размер заполненной очереди.
        self.size = 0

    def is_empty(self):
    """Метод проверяет, пуста ли очередь."""
        return self.size == 0

    def is_full(self):
    """Метод проверяет, заполнена ли очередь."""
        return self.size == self.max_n

    def push_back(self, value):
    """Метод добавляет значение в конец очереди."""
        # Помещаем входящее значение в конец 
        self.deque[self.tail] = value
        # Смещаем индекс первой пустой ячейки.
        self.tail = (self.tail + 1) % self.max_n
        # Увеличиваем размер очереди.
        self.size += 1

    def push_front(self, value):
    """Метод добавляет значение в начало очереди."""
        # Сразу смещаем индекс первого эл-та в очереди.
        self.head = (self.head - 1 + self.max_n) % self.max_n
        # Добавляем в него входящее значение.
        self.deque[self.head] = value
        # Увеличиваем размер очереди.
        self.size += 1

    def pop_back(self):
    """Удаляем последний элемент очереди."""
        # Для начала проверяем не пуста ли очередь.
        if self.is_empty():
            return 'error'
        # Смещаем индекс хвоста на -1.
        # Теперь он указывает на последнее значение.
        self.tail = (self.tail - 1 + self.max_n) % self.max_n
        # Запоминаем это значение для вывода.
        pop_value = self.deque[self.tail]
        # Удаляем это значение из очереди.
        self.deque[self.tail] = None
        # Уменьшаем размер очереди.
        self.size -= 1
        return pop_value

    def pop_front(self):
    """Удаляем первый элемент очереди."""
        # Для начала проверяем не пуста ли очередь.
        if self.is_empty():
            return 'error'
         # Запоминаем значение для вывода.
        pop_value = self.deque[self.head]
        # Удаляем это значение из очереди.
        self.deque[self.head] = None
        # Смещаем индекс головы на первый элемент в очереди.
        self.head = (self.head + 1) % self.max_n
        # Уменьшаем размер очереди.
        self.size -= 1
        return pop_value

def deque_process(max_size, commands):
    """
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
    for command in commands:
        # Проверку на полную очередь я перенес сюда, 
        # убрав из методов класса, т.к. условия вывода из задания
        # заставили бы меня сильно усложнить там код.
        if ((command[0] in push_commands) and deque.is_full()):
            print('error')
        elif command[0] == 'push_back':
            deque.push_back(int(command[1]))
        elif command[0] == 'push_front':
            deque.push_front(int(command[1]))
        elif command[0] == 'pop_back':
            print(deque.pop_back())
        elif command[0] == 'pop_front':
            print(deque.pop_front())

def read_input():
    count_commands = int(input())
    max_size = int(input())
    commands = []
    for _ in range(count_commands):
        commands.append(input().strip().split())
    return max_size, commands

def main():
    max_size, commands = read_input()
    deque_process(max_size, commands)

if __name__ == '__main__':
    main()
