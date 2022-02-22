import sys ; sys.stdin = open('11573.txt')

TC = int(input())


def push(item):
    stack.append(item)


def pop():
    if len(stack) == 0:
        return
    else:
        return stack.pop(-1)


for tc in range(1, TC+1):
    N = int(input())
    lst = list(map(int, input().split()))
    stack = []

    for i in range(N):
        if lst[i] != 0:
            push(lst[i])
        else:
            pop()

    print(f'#{tc} {sum(stack)}')


