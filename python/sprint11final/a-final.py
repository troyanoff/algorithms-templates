# 75236052
def nearest_zero(n, arr):
    # Сразу создаем список с n-кол-вом нулей.
    result = [0] * n
    # Определяем начальное расстояние до нуля.
    offset = 1
    # Задаем отрицательное число, чтобы проверка на первый ноль удалась.
    first_zero_index = -1
    # Прогоняем на поиск ненулей и определяем индекс первого нуля.
    for index, value in enumerate(arr):
        if value != 0:
            result[index] = 1
        elif first_zero_index == -1:
            first_zero_index = index
    # После чего определяем расстояние от левого нуля путем счетчика.
    for index, value in enumerate(result):
        if value == 0:
            offset = 1
        else:
            result[index] = offset
            offset += 1
    # Прогоняем в обратном направлении для определения расстояния до правого нуля.
    for index in range(len(result)-1, -1, -1):
        value = result[index]
        # При переходе через 0 смещение определяем равным 1.
        if value == 0:
            offset = 1
        # Встречая элемент, который больше смещения от правого нуля,
        # убеждаемся, что середина между нулями не достигнута.
        # Присваиваем элементу актуальное смещение и обновляем смещение.
        elif value > offset:
            result[index] = offset
            offset += 1
    # Остается только заменить первые значения в случае, когда первый элемент != 0.
    # Определение и присваивание смещения ранее было завязано на переходе через ноль
    # или же достижения середины между нулями, не обращая внимание на то, что 
    # впедери нуля нет(при прогоне справа на лево), доверяя прогону слева на право.
    # Таким образом, ряд чисел, расположенный до первого нуля,
    # также соответствует данным критериям и расположен "домиком", например: 123210.
    if first_zero_index != 0:
        for first_offset in range(first_zero_index, first_zero_index // 2, -1):
            result[first_zero_index - first_offset] = first_offset
    return result

def read_input():
    n = int(input())
    arr = [int(value) for value in input().strip().split()]
    return n, arr

def main():
    n, arr = read_input()
    print(*nearest_zero(n, arr))

if __name__ == '__main__':
    main()
