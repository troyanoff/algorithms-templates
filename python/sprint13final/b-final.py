# 79168226
# Получилось в полтора раза дольше.
class Participant:
    """Участники соревнования и их результаты."""

    def __init__(self, name: str, result: int, fine: int):
        """Определяет имя, количество решенных задач и размер штрафа."""
        self.name = name
        self.result = result
        self.fine = fine
    

    def __lt__(self, other):
        """Операция сравнения для знака "строго меньше"."""
        if self.result == other.result:
            if self.fine == other.fine:
                return self.name > other.name
            else:
                return self.fine > other.fine
        return self.result < other.result

    def __str__(self):
        """Строковое представление экземпляра - имя участника."""
        return self.name


def econ_quick_sort(arr, left, right):
    """Сортирует участников по убыванию их результатов."""
    # Т.к. сравнение опорного элемента с самим собой в обоих частях массива
    # возвращает фолс, стоит базовый случай стоит определить как массив из двух
    # эл-тов, сравнить их и закончить сортировку.
    if right - left < 2:
        if arr[left] < arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
        return
    # Определяем опорный индекс. Брать центральный == рандом.
    pivot = (left + right) // 2  
    # Запоминаем опорный элемент.
    arr_pivot = arr[pivot]
    # Запоминаем начальный сегмент, для верного определения сторон в будущем.
    right_start = right
    left_start = left
    # След. блок будет выполняться пока не сойдутся указатели окончаний.
    while right > left:
        # Двигаем левый указатель, пока он соответсвует условиям.
        while arr[left] > arr_pivot and left < right:
                left += 1
        # Аналогично правый.
        while arr[right] < arr_pivot and left <= right:
                right -= 1
        # Если нашлись не соответсвующие условиям эл-ты, меняем их местами.
        if right > left:
            arr[left], arr[right] = arr[right], arr[left]
            
    # После распределения по сторонам, проделываем тоже самое уже в рамках
    # этих сторон.
    econ_quick_sort(arr, left_start, right)
    econ_quick_sort(arr, left, right_start)

def read_input():
    count = int(input())
    participants = [
        Participant(name, int(result), int(fine))
        for name, result, fine
        in (
            input().strip().split() for _ in range(count)
        )
    ]
    return count, participants

def main():
    count, participants = read_input()
    econ_quick_sort(participants, 0, count - 1)
    print(*participants, sep='\n')

if __name__ == '__main__':
    main()
