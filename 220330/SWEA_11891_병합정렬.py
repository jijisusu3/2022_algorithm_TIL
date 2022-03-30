import sys;
sys.stdin = open('11891.txt')


def merge_sort(s, e):
    global cnt
    if s == e:
        return
    mid = (s + e - 1) // 2
    merge_sort(s, mid)
    merge_sort(mid + 1, e)
    if arr[mid] > arr[e]:
        cnt += 1
    i, j, k = s, mid + 1, s
    while i <= mid and j <= e:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            k, i = k + 1, i + 1
        else:
            tmp[k] = arr[j]
            k, j = k + 1, j + 1
    while i <= mid:
        tmp[k] = arr[i]
        k, i = k + 1, i + 1
    while j <= e:
        tmp[k] = arr[j]
        k, j = k + 1, j + 1

    for i in range(s, e + 1):
        arr[i] = tmp[i]


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    tmp = [0] * N
    merge_sort(0, N - 1)
    print(f'#{tc} {arr[N//2]} {cnt}')