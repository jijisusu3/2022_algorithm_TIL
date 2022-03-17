import sys

sys.stdin = open('5174.txt')


def count(node):
    global cnt
    if node == 0:
        return
    count(L[node])
    cnt += 1
    count(R[node])


TC = int(input())
for tc in range(1, TC + 1):
    cnt = 0
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    L = [0] * (E + 2)
    R = [0] * (E + 2)
    for i in range(0, 2*E, 2):
        p, c = lst[i], lst[i + 1]
        if L[p]:
            R[p] = c
        else:
            L[p] = c
    count(N)
    print(f'#{tc} {cnt}')