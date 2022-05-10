def solution(rows, columns, queries):
    answer = []
    arr = []
    i = 0
    for row in range(rows):
        temp = []
        for col in range(columns):
            i += 1
            temp.append(i)
        arr.append(temp)
    for query in queries:
        r1, c1, r2, c2 = query
        tmp = arr[r1 - 1][c1 - 1]
        min_num = tmp
        for i in range(r1 - 1, r2 - 1):
            arr[i][c1 - 1] = arr[i + 1][c1 - 1]
            min_num = min(min_num, arr[i][c1 - 1])
        for i in range(c1 - 1, c2 - 1):
            arr[r2 - 1][i] = arr[r2 - 1][i + 1]
            min_num = min(min_num, arr[r2 - 1][i])
        for i in range(r2 - 1, r1 - 1, -1):
            arr[i][c2 - 1] = arr[i - 1][c2 - 1]
            min_num = min(min_num, arr[i][c2 - 1])
        for i in range(c2 - 1, c1 - 1, -1):
            arr[r1 - 1][i] = arr[r1 - 1][i - 1]
            min_num = min(min_num, arr[r1 - 1][i])
        arr[r1 - 1][c1] = tmp
        answer.append(min_num)

    return answer
