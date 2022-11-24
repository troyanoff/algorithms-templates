class Stack:
    def __init__(self):
        self.result = []
        
    def push(self, value):
        self.result.append(value)
        
    def action(sign):
        second = self.result.pop()
        first = self.result.pop()
        if sign == '*':
            self.result.append(first * second)
        elif sign == '/':
            self.result.append(first / second)
        elif sign == '+':
            self.result.append(first + second)
        elif sign == '-':
            self.result.append(first - second)
    
    def return_result():
        return self.result[-1]

def calculation(data):
    stack = Stack()
    list_sign = '*/+-'
    for value in data:
        if value in list_sign:
            stack.action(value)
        else:
            stack.push(value)
    return stack.return_result()
        

def read_input():
    return input().strip().split()

def main():
    data = read_input()
    print(calculation(data))

if __name__ == '__main__':
    main()
