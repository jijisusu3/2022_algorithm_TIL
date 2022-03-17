import sys
sys.stdin = open('5177.txt')


def Q(x):
    global n
    n += 1 # 방문
    tree[n] = x
    c = n
    p = n // 2
    while p >= 1 and tree[p] > tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    tree = [0] * (N + 1)
    n = 0 # 노드번호(index) 셀 것
    for x in lst:
        Q(x)
    result = 0
    p = N // 2
    while p:
        result += tree[p]
        p = p // 2
    print(f'#{tc} {result}')
