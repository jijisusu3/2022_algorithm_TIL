import sys
sys.stdin = open('5178.txt')


def add_lr(start):
    if start * 2 <= N and tree[start] == 0:
        add_lr(start * 2)
        tree[start] += tree[start * 2]
    if start * 2 + 1 <= N:
        add_lr(start * 2 + 1)
        tree[start] += tree[start * 2 + 1]


TC = int(input())
for tc in range(1, TC + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for _ in range(M):
        node, num = map(int, input().split())
        tree[node] = num
    add_lr(1)
    result = tree[L]
    print(f'#{tc} {result}')
