def select(lst, th):
    for i in range(0, th):
        x = i
        for j in range(i + 1, len(lst)):
            if lst[x] > lst[j]:
                x = j
        lst[i], lst[x] = lst[x], lst[i]
    return lst[th-1]


def solution(array, commands):
    answer = []
    arr = array
    for i, j, k in commands:
        new_arr = arr[i-1:j]
        th_num = select(new_arr, k)
        answer.append(th_num)
    return answer

