from collections import deque


def bfs(start, end):
    visited = [0] * (V + 1)
    visited[start] = 1
    Q = deque()
    Q.append(start)

    while Q:
        v = Q.popleft() # Q에서 정점을 하나 꺼내온다.
        if v == end:
            return visited[v] - 1
        for w in G[v]: # v의 인접정점을 찾는다.
            if not visited[w]:
                visited[w] = visited[v] + 1
                Q.append(w)
    return visited[end]


TC = int(input())
for tc in range(1, TC + 1):
    V, E = map(int, input().split())
    # 인접 리스트로 저장
    G = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    s, g = map(int, input().split()) # 출발점과 도착점
    result = bfs(s, g)
    print(f'#{tc} {result}')