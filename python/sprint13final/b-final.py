def sort_check_left(num,pivot):
    if int(num[1]) == int(pivot[1]):
        if int(num[2]) == int(pivot[2]):
            return num[0] < pivot[0]
        else:
            return int(num[2]) > int(pivot[2])
    return int(num[1]) < int(pivot[1])

def sort_check_right(num, pivot):
    if int(num[1]) == int(pivot[1]):
        if int(num[2]) == int(pivot[2]):
            return num[0] > pivot[0]
        else:
            return int(num[2]) < int(pivot[2])
    return int(num[1]) > int(pivot[1])

def megasort(n, arr):
    pivot = arr[n//2]
    left = 0
    right = n-1
    while left != right
        arr_left = arr[left]
        arr_pivot = arr[pivot]
        arr_right = arr[right]
        while sort_check_left(arr[left], arr[pivot]):
            left += 1
        while sort_check_right(arr[right], arr[pivot]):
            right -= 1
        arr[left], arr[right] = arr[right], arr[left]
    if n == 1:
        return arr
    return megasort()
    

def read_input():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input().strip().split())
    return n, arr

def main():
    n, arr = read_input()
    result = megasort(n, arr)
    print(*result)

if __name__ == '__main__':
    main()
