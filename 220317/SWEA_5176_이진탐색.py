import sys
sys.stdin = open('5176.txt')


def n_name(start):
    global cnt
    if start <= N:
        n_name(start*2) # 왼쪽
        tree[start] = cnt # 중위 !
        cnt += 1
        n_name(start*2 + 1) # 오른쪽


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    cnt = 1
    tree = [0] * (N + 1)
    n_name(1)
    n = N // 2
    result = tree[n]
    root = tree[1]
    print(f'#{tc} {root} {result}')

