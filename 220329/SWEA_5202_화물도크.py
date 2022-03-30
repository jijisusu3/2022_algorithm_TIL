TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    acts = []
    for _ in range(N):
        acts.append(tuple(map(int, input().split())))
    acts.sort(key=lambda x: x[1])

    ft = acts[0][1]
    ans = 1
    for i in range(1, N):
        if ft <= acts[i][0]:
            ans += 1
            ft = acts[i][1]
    print(f'#{tc} {ans}')