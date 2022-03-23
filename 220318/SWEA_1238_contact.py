import sys
sys.stdin = open('1238.txt')


def bfs(s):
    Q = []
    visited = [0]*101
    Q.append(s)
    visited[s] = 1
    sol = s
    while Q:
        x = Q.pop(0)
        if visited[sol] < visited[x]  or visited[sol] == visited[x] and sol < x:
            sol = x
        for j in range(1, 101):
            if arr[x][j] and visited[j] == 0:
                Q.append(j)
                visited[j] = visited[x] + 1
    return sol


for tc in range(1, 11):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    arr = [[0]*101 for _ in range(101)]
    for i in range(0, len(lst), 2):
        arr[lst[i]][lst[i+1]] = 1
    result = bfs(S)
    print(f'#{tc} {result}')

