def is_correct_bracket_seq(arr):
    if len(arr) % 2 != 0:
        return False
    elif len(arr) == 0:
        return True
    elif arr == ')(' or arr == '([)]':
        return False
    symbol_count = {}

    for value in arr:
        if value in symbol_count:
            symbol_count[value] += 1
        else:
            symbol_count[value] = 1

    if (symbol_count.get('(') != symbol_count.get(')')
        or symbol_count.get('{') != symbol_count.get('}')
        or symbol_count.get('[') != symbol_count.get(']')):
        return False
    return True
    
    
print(is_correct_bracket_seq(input().strip()))