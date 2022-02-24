import sys ; sys.stdin = open('1224.txt')

for tc in range(1, 11):
    N = int(input())
    lst = list(input())
    box = []
    stack = []
    prior = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1, ')': 1}

    for token in lst:
        if token.isdigit():
            box.append(int(token))

        elif token == '(':
            stack.append(token)
        elif token == ')':
            temp = stack.pop()
            while temp != '(':
                box.append(temp)
                temp = stack.pop()

        else:
            while stack and prior[token] <= prior[stack[-1]]:
                box.append(stack.pop())
            stack.append(token)

    while stack:
        box.append(stack.pop())

    for i in box:
        if i in prior:
            b = stack.pop()
            a = stack.pop()
            if i == '+':
                stack.append(a + b)
            elif i == '-':
                stack.append(a - b)
            elif i == '*':
                stack.append(a * b)
            elif i == '/':
                stack.append(a / b)
        else:
            stack.append(i)
    print(f'#{tc} {stack[0]}')