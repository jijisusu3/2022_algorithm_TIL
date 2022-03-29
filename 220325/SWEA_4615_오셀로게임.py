TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N + 1)]
    arr[N // 2][N // 2] = arr[N // 2 + 1][N // 2 + 1] = 1 # 초기값 가운데에 놓기
    arr[N // 2 + 1][N // 2] = arr[N // 2][N // 2 + 1] = 2

    for _ in range(M):
        sj, si, d = map(int, input().split())
        arr[si][sj] = d
        for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)):
            s = []
            for k in range(1, N):
                ni, nj = si + di*k, sj + dj*k
                if 1<= ni < N and 1 <= nj < N:
                    if arr[ni][nj] == 0:
                        break
                    elif arr[ni][nj] == d:
                        for ci, cj in s:
                            arr[ci][cj] = d
                    else:
                        s.append((ni, nj))
                else:
                    break

    black = white = 0
    for lst in arr:
        black += lst.count(1)
        white += lst.count(2)
