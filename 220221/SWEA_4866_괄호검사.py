import sys ; sys.stdin = open('4866.txt')

TC = int(input())
for tc in range(1, TC+1):
    lst = list(input())
    stack = []
    for i in lst:
        if i == '(' or i == '{':
            stack.append(i)
        elif i == ')' or i == '}':
            if len(stack) == 0:
                stack = [1]
                break
            elif i == ')' and stack[-1] != '(':
                stack = [1]
                break
            elif i == '}' and stack[-1] != '{':
                stack = [1]
                break
            else:
                stack.pop(-1)

    if len(stack) == 0:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)


