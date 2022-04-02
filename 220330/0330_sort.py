def quick_sort(s, e):
    if s >= e: return
    # 파티션
    i, j = s, e
    while i < j:
        while i <= e and arr[s] >= arr[i]:
            i += 1
        while arr[s] < arr[j]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # 헤쳐모여 끝났으므로 arr[s]와 arr[j]를 교환
    arr[s], arr[j] = arr[j], arr[s]
    quick_sort(s, j - 1)
    quick_sort(j + 1, e)


arr = [7, 5, 8, 4, 1, 2, 10, 4, 3, 6, 9, 8]
# arr = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
N = len(arr)
quick_sort(0, N - 1)
print(arr)
