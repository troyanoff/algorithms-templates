def search_target(nums, target, left, right):
    len_nums = right - left
    mid = len_nums // 2
    nums_mid = nums[mid]
    if len_nums == 0:
        return -1
    elif len_nums == 1 and nums[0] != target:
        return -1
    elif nums_mid == target:
        return mid + left
    elif nums_mid > target:
        return search_target(nums[:mid], target, left, left + mid)
    else:
        return search_target(nums[mid:], target, left + mid, right)

def search_start(nums, left, right):
    len_nums = right - left
    mid = len_nums // 2
    nums_mid = nums[mid]
    if len_nums == 1:
        return nums[0]
    elif len_nums == 0:
        return "ашипка"
    elif nums_mid < nums[mid-1]:
        return left + mid
    else:
        if nums[-1] > nums_mid:
            return search_start(nums[:mid], left, left + mid)
        else:
            return search_start(nums[mid:], left + mid, right)

def check_broken(arr):
    return arr[0] > arr[-1]

def check_target(arr, target, broken):
    if broken:
        return arr[0] <= target
    else:
        return arr[0] <= target <= arr[-1]

def normal_search(nums, target, left, right):
    mid = (right - left) // 2
    if not check_broken(nums):
        return nums, left, right
    nums_mid = nums[:mid]
    nums_mid_ = nums[mid:]
    broken_left = check_broken(nums_mid)
    left_target = check_target(nums_mid, target, broken_left)
    if broken_left:
        if left_target:
            return normal_search(nums_mid, target, left, mid + left)
        else:
            return nums_mid_, mid + left, right
    else:
        if left_target:
            return nums_mid, left, mid + left
        else:
            return normal_search(nums_mid_, target, mid + left, right)

def broken_search(nums, target) -> int:
    len_nums = len(nums)
    start = search_start(nums, 0, len_nums)
    if nums[0] > nums[start]:
        return search_target(nums[start:], target, start, len_nums)
    else:
        return search_target(nums[:start], target, 0, start)
    # normal, left, right = normal_search(nums, target, 0, len_nums)
    # try:
    #     return normal.index(target) + left
    # except:
    #     return -1
    # if len(normal) == 0:
    #     return -1
    # else:
    #     return search_target(normal, target, left, right)

def read_input():
    n = 14
    target = 5
    arr = [19, 21, 100, 101, 102, 1, 5, 7, 12, 13, 14, 15, 16, 17]
    #n = int(input())
    #target = int(input())
    #arr = [int(value) for value in input().strip().split()]
    return arr, target

def main():
    arr, target = read_input()
    print(broken_search(arr, target))

if __name__ == '__main__':
    main()
