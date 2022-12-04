def dress_sort(n, arr):
    count = [0, 0,0]
    result = []
    for i in arr:
        count[i] += 1
    result += [0] * count[0]
    result += [1] * count[1]
    result += [2] * count[2]
    return ' '.join(result)            

n = int(input())
arr = list(map(int, input().strip().split()))
dress_sort(n,arr)