A, B = map(str, input().split())
N = len(A)
M = len(B)
arr = [['.']*N for _ in range(M)]
findA, findB = 0, 0
breaker = False
for i in range(N):
    for j in range(M):
        if A[i] == B[j]:
            findA = i
            findB = j
            breaker = True
            break
    if breaker:
        break

for x in range(M):
    arr[x][findA] = B[x]
for y in range(N):
    arr[findB][y] = A[y]

for i in range(M):
    temp = ''
    for j in range(N):
        temp += arr[i][j]
    print(temp)







