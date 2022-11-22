def square(n, m):
    result = []
    result_output = ''
    shift = 0
    for i in range(len(min(n,m))-1, -1, -1):
        value = int(n[i]) + int(m[i]) + shift
        if value < 2:
            result.append(str(value))
            shift = 0
        elif value == 2:
            result.append('0')
            shift = 1
        elif value == 3:
            result.append('1')
            shift = 1
    offset = len(max(n,m))-len(min(n,m))
    for i in range(offset, 0, -1):
        if shift == 1 and max(n,m)[i] == '1':
            result.append('0')
        elif shift == 1 and max(n,m)[i] == '0':
            result.append('1')
            shift = 0
        else:
            result.append(max(n,m)[i])
    if shift == 1:
        result.append('1')
    for i in range(len(result)-1, -1, -1):
        result_output += result[i]


    return result_output

def read_input():
    n = str(input())
    m = str(input())
    return n, m

n, m = read_input()
print(square(n, m))
