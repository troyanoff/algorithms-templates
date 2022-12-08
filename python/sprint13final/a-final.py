# 79022022
def search_target(nums, target, left, right):
    """Ищет элемент в сломанном массиве без повторов.
    
    Принимает на вход массив, искомый элемент(ИЭ), значения левого и правого
    индекса. Определяет месторасположение(индекс) ИЭ в массиве по логике 
    бинарного поиска, с вынужденным определением "сломанной" стороны массива. 
    """
    # Находим середину рассматриваемого диапазона.
    mid = (right + left) // 2
    # Запоминаем сразу значения левого, правого и серединного эл-тов.
    num_mid = nums[mid]
    num_right = nums[right]
    num_left = nums[left]
    # Сравниваем ИЭ с имеющимися в распоряжении значениями.
    # Это экономит время и решает проблему с массивами длинны <=3
    if num_mid == target:
        return mid
    elif num_left == target:
        return left
    elif num_right == target:
        return right
    # Если дошли до этого блока с массивом длинной 2, точно ИЭ здесь нет.
    elif right - left <= 1:
        return -1
    # Далее произвольно выбираем сторону для проверки. Я выбрал право.
    # Сломан ли правый массив.
    elif num_mid > num_right:
        # Если сломан правый, проверяем, в нем ли ИЭ.
        if target > num_mid or target < num_left:
            return search_target(nums, target, mid+1, right)
        # Если не в правом, то остается только левый.
        else:
            return search_target(nums, target, left, mid-1)
    else:
        # Если правый не сломан, проверяем совсем по другому
        # на наличие ИЭ в правом массиве.
        # Т.о., в случае, когда массив не сломан, все будет работать хорошо.
        if num_mid < target < num_right:
            return search_target(nums, target, mid+1, right)
        else:
            # Получается левый.
            return search_target(nums, target, left, mid-1)

def broken_search(nums, target) -> int:
    """Филигранно определяет длинну массива."""
    # Предоставленная сигнатура не предполагает передачу длинны массива,
    # хотя на ввод предполагается ее подача.
    # Поэтому находим длинну массива для объявления правого эл-та.
    len_nums = len(nums)
    left = 0
    right = len_nums - 1
    # Передаем в рекурсивную вспомогательную функцию поиска
    # и выводим ее результат.
    return search_target(nums, target, left, right)

# def read_input():
#     n = int(input())
#     target = int(input())
#     arr = [int(value) for value in input().strip().split()]
#     return arr, target

# def main():
#     arr, target = read_input()
#     print(broken_search(arr, target))

# if __name__ == '__main__':
#     main()
