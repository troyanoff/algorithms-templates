def search_start(nums):
    len_nums = len(nums)
    if len_nums == 1:
        return nums[0][0]
    mid = len_nums // 2
    if nums[mid][1] < nums[mid-1][1]:
        return  nums[mid][0]
    else:
        search_start(nums[:mid])
        search_start(nums[mid:])

def search_target(nums, target):
    absent = -1
    for index, value in nums:
        if value == target:
            return index
    return absent

def broken_search(nums, target) -> int:
    if target not in nums:
        return -1
    enumerate_nums = list(enumerate(nums))
    start = search_start(enumerate_nums)
    if nums[0] > target:
        return search_target(enumerate_nums[start:], target)
    else:
        return search_target(enumerate_nums[:start], target)

def read_input():
    n = int(input())
    target = int(input())
    arr = [int(value) for value in input().strip().split()]
    return arr, target

def main():
    arr, target = read_input()
    print(broken_search(arr, target))

if __name__ == '__main__':
    main()
