def dijkstra(n):
    D = [0xfffff] * (N + 1)
    visit = [0] * (N + 1)
    D[n] = 0

    cnt = N
    while cnt:
        s, val = 0, 0xfffff
        for i in range(1, N + 1):
            if not visit[i] and D[i] < val:
                s, val = i, D[i]

        visit[s] = 1

        for e, w in G[s]:
            if not visit[e] and D[e] > D[s] + w:
                D[e] = D[s] + w
        cnt -= 1
    print(f'#{tc} {D[N]}')


for tc in range(1, int(input()) + 1):
    N, E = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        G[s].append((e, w))
    dijkstra(0)