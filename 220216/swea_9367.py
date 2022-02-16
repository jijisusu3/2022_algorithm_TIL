T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 1
    max_v = 1

    for i in range(1, N):
        if arr[i] > arr[i - 1]:
            cnt += 1
            if max_v < cnt:
                max_v = cnt
        else:
            cnt = 1

    print(f'#{tc} {max_v}')
