import sys
sys.stdin = open('11899.txt')


def find_set(x):
    if x != P[x]:
        P[x] = find_set(P[x])
    return P[x]


TC = int(input())

for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    mst = []
    cnt = 0
    P = [i for i in range(N+1)]
    for i in range(0, M*2, 2):
        u, v = lst[i], lst[i + 1]
        a = find_set(u)
        b = find_set(v)
        if a != b:
            P[a] = b
            cnt += 1
    result = N - cnt
    print(f'#{tc} {result}')
