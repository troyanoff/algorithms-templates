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

    # Метод проверяет, пуста ли очередь.
    def is_empty(self):
        return self.size == 0

    # Метод проверяет, заполнена ли очередь.
    def is_full(self):
        return self.size == self.max_n

    # Метод добавляет значение в конец очереди.
    def push_back(self, value):
        # Помещаем входящее значение в конец 
        self.deque[self.tail] = value
        self.tail = (self.tail + 1) % self.max_n
        self.size += 1

    def push_front(self, value):
        if self.is_full():
            return 'error'
        self.head = (self.head - 1 + self.max_n) % self.max_n
        self.deque[self.head] = value
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            return 'error'
        self.tail = (self.tail - 1 + self.max_n) % self.max_n
        pop_value = self.deque[self.tail]
        self.deque[self.tail] = None
        self.size -= 1
        return pop_value

    def pop_front(self):
        if self.is_empty():
            return 'error'
        pop_value = self.deque[self.head]
        self.deque[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return pop_value

def deque_process(max_size, commands):
    deque = Deque(n = max_size)
    for command in commands:
        if ((command[0] == 'push_back' or command[0] == 'push_front')
            and deque.is_full()):
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
