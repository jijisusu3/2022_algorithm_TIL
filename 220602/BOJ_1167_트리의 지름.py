import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n + 1)]


for _ in range(n):
    lst = map(int, input().split())
    for i in range(1, len(lst) - 2, 2):
        tree[lst[0]].append((lst[i], lst[i+1]))


def bfs(start):
    visited = [-1] * (n + 1)
    Q = deque()
    Q.append(start)
    visited[start] = 0
    max_result = [0, 0]

    while Q :
        temp = Q.popleft()
        for node, distance in tree[temp]:
            if visited[node] == -1:


