def bfs(x, total, count):
    global result
    if count == N - 1:
        if result > total + arr[x][1]:
            result = total + arr[x][1]

    for i in range(2, N + 1):
        if visited[i] == 0:
            visited[i] = 1
            bfs(i, total + arr[x][i], count + 1)
            visited[i] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * (N + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 2)]
    visited = [0] * (N + 1)
    visited[1] = 1
    result = (N**2)*100
    value = 0
    cnt = 0
    bfs(1, value, cnt)
    print(f'#{tc} {result}')