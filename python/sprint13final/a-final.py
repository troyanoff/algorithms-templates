def search_target(nums, target, left, right):
    len_nums = len(nums)
    mid = len_nums // 2
    if len_nums == 0:
        return -1
    elif len_nums == 1 and nums[0] != target:
        return -1
    elif nums[mid] == target:
        return mid + left
    elif nums[mid] > target:
        return search_target(nums[:mid], target, left, left + mid)
    else:
        return search_target(nums[mid:], target, left + mid, right)

def check_broken(arr):
    return arr[0] > arr[-1]

def check_target(arr, target, broken):
    if broken:
        return arr[0] <= target
    else:
        return arr[0] <= target <= arr[-1]

def normal_search(nums, target, left, right):
    mid = len(nums) // 2
    if not check_broken(nums):
        return nums, left, right
    broken_left = check_broken(nums[:mid])
    left_target = check_target(nums[:mid], target, broken_left)
    if broken_left:
        if left_target:
            return normal_search(nums[:mid], target, left, mid + left)
        else:
            return nums[mid:], mid + left, right
    else:
        if left_target:
            return nums[:mid], left, mid + left
        else:
            return normal_search(nums[mid:], target, mid + left, right)

def broken_search(nums, target) -> int:
    len_nums = len(nums)
    mid = len_nums // 2
    normal, left, right = normal_search(nums, target, 0, len_nums)
    if len(normal) == 0:
        return -1
    else:
        return search_target(normal, target, left, right)

def read_input():
    n = 9
    target = 5
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    #n = int(input())
    #target = int(input())
    #arr = [int(value) for value in input().strip().split()]
    return arr, target

def main():
    arr, target = read_input()
    print(broken_search(arr, target))

if __name__ == '__main__':
    main()
