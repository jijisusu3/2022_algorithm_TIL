# 퀵정렬


def quick_sort(s, e):
    if s >= e: return
    # 파티션
    i, j = s, e
    while i < j:
        while arr[s] >= arr[i]:  # 한쪽에만  = 조건 넣어줘야함
            i += 1
        while arr[s] < arr[j]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # 헤쳐모여 끝났으므로 arr[s]와 arr[j]를 교환
    arr[s], arr[j] = arr[j], arr[s]
    quick_sort(s, j - 1)
    quick_sort(j + 1, e)


arr = [7, 34, 5, 76, 2, 1, 3, 19, 50]
N = len(arr)
quick_sort(0, N - 1)
print(arr)