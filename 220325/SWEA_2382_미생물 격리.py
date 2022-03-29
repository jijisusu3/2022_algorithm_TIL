TC = int(input())
di, dj = (-1, 1, 0, 0), (0, 0, -1, 1)
opp = (0, 2, 1, 4, 3)
for tc in range(1, TC + 1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)]
    for _ in range(M):
        for i in range(len(arr)):
            arr[i][0] = arr[i][0] + di[arr[i][3]]
            arr[i][1] = arr[i][1] + dj[arr[i][3]]
            # 가장자리로 왔을 때
            if arr[i][0] == 0 or arr[i][0] == N-1 or arr[i][1] == 0 or arr[i][1] == N-1:
                arr[i][2] //= 2
                arr[i][3] = opp[arr[i][3]]
            # 합치기 (내림차순)
            arr.sort(key=lambda x:  (x[0], x[2]), reverse=True)

            i = 1
            while i < len(arr):
                if arr[i-1][0] == arr[i][0] and arr[i-1][1] == arr[i][1]:
                    arr[i-1][2] += arr[i][2]
                    arr.pop(i)
                else:
                    i += 1

    ans = 0
    for i in range(len(arr)):
        ans += arr[i][2]
    print(ans)