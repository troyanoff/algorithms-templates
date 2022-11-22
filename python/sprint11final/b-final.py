# 75238891
def click_ability(n, arr):
    result = 0
    # Определяем озможность нажатий у двух человек.
    clicks = n * 2
    # Проверяем есть ли числа 1-9 в массиве и подсчитываем их количество.
    for digit in range(1, 10):
        str_digit = str(digit)
        if 0 < arr.count(str_digit) <= clicks:
            # Если хватает нажатий для количества цифр, начисляем балл.
            result += 1
    return result

def read_input():
    n = int(input())
    keypad = ''
    for _ in range(4):
        keypad += input()
    return n, keypad

def main():
    n, arr = read_input()
    print(click_ability(n, arr))

if __name__ == '__main__':
    main()
