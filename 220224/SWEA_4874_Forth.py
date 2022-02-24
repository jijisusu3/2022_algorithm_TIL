import sys;
sys.stdin = open('4874.txt')

TC = int(input())
for tc in range(1, TC + 1):
    box = list(map(str, input().split()))
    stack = []
    try:
        for token in box[:-1]:
            if token in '+-*/':
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        if len(stack) == 1:
            print(f'#{tc} {stack[0]}')
        else:
            print(f'#{tc} error')
    except:
        print(f'#{tc} error')
