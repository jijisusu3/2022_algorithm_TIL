# 블랙잭


# 시간초과
import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

max_num = 0
for i in range(1 << N):
    temp_lst = []
    for j in range(N):
        if i & (1 << j):
            temp_lst.append(arr[j])
    if len(temp_lst) == 3:
        temp_add = sum(temp_lst)
        if max_num < temp_add <= M:
            max_num = temp_add
print(max_num)


# for문 이용
result = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if arr[i] + arr[j] + arr[k] > M:
                continue
            else:
                result = max(result, arr[i] + arr[j] + arr[k])
print(result)