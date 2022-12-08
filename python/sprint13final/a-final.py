def search_target(nums, target, left, right):
    mid = (right + left) // 2
    num_mid = nums[mid]
    num_right = nums[right]
    num_left = nums[left]
    if right - left <= 1 and target not in (num_left, num_right, num_mid):
        return -1
    elif num_mid == target:
        return mid
    elif num_left == target:
        return left
    elif num_right == target:
        return right
    elif num_mid > num_right:
        if target < num_mid and target < num_right:
            return search_target(nums, target, mid, right)
        else:
            return search_target(nums, target, left, mid)
    else:
        if num_mid < target < num_right:
            return search_target(nums, target, mid, right)
        else:
            return search_target(nums, target, left, mid)

def broken_search(nums, target) -> int:
    len_nums = len(nums)
    left = 0
    right = len_nums - 1
    return search_target(nums, target, left, right)

def read_input():
    n = 2#9
    target = 1#5
    arr = [0]#[19, 21, 100, 101, 102, 1, 5, 7, 12]
    #n = int(input())
    #target = int(input())
    #arr = [int(value) for value in input().strip().split()]
    return arr, target

def main():
    arr, target = read_input()
    print(broken_search(arr, target))

if __name__ == '__main__':
    main()
