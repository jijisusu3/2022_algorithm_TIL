import sys;

sys.stdin = open('11898.txt')

from collections import deque


def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == M:
            return lst[x]
        for now in (x - 1, x + 1, 2 * x, x - 10):
            if 0 <= now <= 1000000 and lst[now] == 0:
                lst[now] = lst[x] + 1
                q.append(now)


TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    lst = [0] * 1000001
    result = bfs()
    print(f'#{tc} {result}')
