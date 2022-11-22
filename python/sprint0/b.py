from typing import List, Tuple

def zipper(a: List[int], b: List[int]) -> List[int]:
    final_list = []
    for i in range(len(a)):
        final_list.append(a[i])
        final_list.append(b[i])
    return final_list

def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b

a, b = read_input()
print(" ".join(map(str, zipper(a, b))))
