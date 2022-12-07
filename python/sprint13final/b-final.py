# 78957608
def check_left(participant, pivot):
    """Проверяет, что участник сильнее опорного."""
    # Распаковываем информацию, для экономии времени.
    part_name, part_result, part_fine = participant
    pivot_name, pivot_result, pivot_fine = pivot
    # При равном кол-ве решенных задач, проверяем штраф.
    if part_result == pivot_result:
        # При равном штрафе, проверяем насколько сильно их имя.
        if part_fine == pivot_fine:
            # Чем unicode-шифр больше, тем слабее имя.
            return part_name < pivot_name
        else:
            # Если штраф меньше, участник сильнее.
            return part_fine < pivot_fine
    # Если предыдущий блок пропущен, проверяем кол-во задач.
    return part_result > pivot_result

def check_right(participant, pivot):
    """Проверяет, что участник слабее опорного."""
    # Логика обратная той, что в функции check_left.
    part_name, part_result, part_fine = participant
    pivot_name, pivot_result, pivot_fine = pivot
    if part_result == pivot_result:
        if part_fine == pivot_fine:
            return part_name > pivot_name
        else:
            return part_fine > pivot_fine
    return part_result < pivot_result

def econ_quick_sort(count, arr):
    """Сортирует участников по убыванию их результатов."""
    # Если массив стал пустым или с одним эл-том, возвращаем результат.
    if count < 2:
        return arr
    # Определяем опорный индекс. Брать центральный == рандом.
    pivot = count // 2
    # Определяем индексы окончаний списка участников.
    left = 0
    right = count - 1
    # Запоминаем опорный элемент.
    arr_pivot = arr[pivot]
    # След. блок будет выполняться пока не сойдутся указатели окончаний.
    while right != left:
        # Двигаем левый указатель, пока он соответсвует условиям.
        while check_left(arr[left], arr_pivot):
            left += 1
        # Аналогично правый.
        while check_right(arr[right], arr_pivot):
            right -= 1
        # Если нашлись не соответсвующие условиям эл-ты, меняем их местами.
        arr[left], arr[right] = arr[right], arr[left]
    # Соединяем массив тех, кто сильнее, с теми, кто слабее.
    # В качестве длинны массива на левую сторону передаем указатель(они равны),
    # а на правый, оставшееся до длинный массива число эл-тов.
    return (econ_quick_sort(right, arr[:right])
            + econ_quick_sort(count - right, arr[right:]))

def read_input():
    count = int(input())
    participants = []
    for _ in range(count):
        # Во избежание множественных переводов в int в функциях проверки,
        # сразу изменяем тип данных у кол-ва задач и штрафа.
        participant = input().strip().split()
        participant[1] = int(participant[1])
        participant[2] = int(participant[2])
        participants.append(participant)
    return count, participants

def main():
    count, participants = read_input()
    result = econ_quick_sort(count, participants)
    for participant in result:
        print(participant[0])

if __name__ == '__main__':
    main()
