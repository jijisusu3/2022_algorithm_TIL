import sys;
sys.stdin = open('5251.txt')

TC = int(input())
for tc in range(1, TC + 1):
    N, E = map(int, input().split())
    G = [[] for _ in range(N + 1)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        G[u].append((v, w))

    # 거리를 저장하는 배열
    D = [0xffffff] * (N + 1)
    D[0] = 0

    while True:
        flag = True
        for u in range(0, N + 1):
            for v, w in G[u]:
                if D[v] > D[u] + w:
                    D[v] = D[u] + w
                    flag = False
        if flag:
            break
    print(f'#{tc} {D[N]}')