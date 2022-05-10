from collections import deque


def bfs(start, cnt):
    Q = deque()
    Q.append((start, cnt))
    visited[start] = True
    while Q:
        x, y = Q.popleft()
        if x == 100:
            return y
        for dice in range(1, 7):
            next_go = x + dice
            if 1 <= next_go <= 100:
                if next_go in ladder:
                    next_go = ladder[next_go]
                if next_go in snake :
                    next_go = snake[next_go]
                if not visited[next_go]:
                    Q.append((next_go, y + 1))
                    visited[next_go] = True


N, M = map(int, input().split())
visited = [False] * 101
ladder, snake = dict(), dict()
for _ in range(N):
    s, e = map(int, input().split())
    ladder[s] = e
for _ in range(M):
    s, e = map(int, input().split())
    snake[s] = e

print(bfs(1, 0))
