from collections import deque


def land(row, col):
    Q = deque()
    Q.append((row, col))
    while Q:
        a, b = Q.popleft()
        nr = a +





N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited_1 = [[0]*N for _ in range(N)]

for r in range(N):
    for c in range(N):
        if visited_1[r][c] == 0 and arr[r][c] == 1:


print(arr)
