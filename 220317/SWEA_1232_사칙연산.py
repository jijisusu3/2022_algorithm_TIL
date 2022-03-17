import sys
sys.stdin = open('1232.txt')


def post_order(v):
    global result
    if not tree[v] in cals:  # 숫자
        return tree[v]
    else:  # 연산자
        left = post_order(L[v])
        right = post_order(R[v])
        if tree[v] == '+':
            result = left + right
        elif tree[v] == '-':
            result = left - right
        elif tree[v] == '*':
            result = left * right
        elif tree[v] == '/':
            result = left // right
        return result


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    cals = ['+', '-', '*', '/']
    for i in range(N):
        temp = input().split()
        p, cal = int(temp[0]), temp[1]
        if cal not in cals: # 숫자일 때
            tree[p] = int(cal)
        else: # 연산자일 때
            tree[p] = cal
        if len(temp) == 4:
            L[p] = int(temp[2])
            R[p] = int(temp[3])
    result = 0
    post_order(1)
    print(f'#{tc} {result}')

