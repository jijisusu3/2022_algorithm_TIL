def angle(x1, y1, x2, y2):  # 각도구하기!!!!
    return (y2 - y1) / (x2 - x1)


N = int(input())
buildings = [0] + list(map(int, input().split())) # index + 1 (1부터 시작하니까)
result = 0
x1 = 0
for y1 in buildings[1:]:  # 빌딩 순서대로 하나씩 가져와.
    x1 += 1  # idx

    # 오른쪽에서 보이는 빌딩
    right = 0
    standard_right = None
    for x2 in range(x1 + 1, N + 1):  # idx 다음꺼 부터 N까지
        y2 = buildings[x2]
        temp = angle(x1, y1, x2, y2)
        if standard_right is None or standard_right < temp:  # None일 때는 처음! 처음일때는 항상 보임
            standard_right = temp
            right += 1
    # 왼쪽에서 보이는 빌딩
    left = 0
    standard_left = None
    for x2 in range(x1 - 1, 0, -1):
        y2 = buildings[x2]
        temp = angle(x1, y1, x2, y2)
        if standard_left is None or standard_left > temp:  # None일 때는 처음! 처음일때는 항상 보임
            standard_left = temp
            left += 1

    if (right + left) > result:
        result = (right + left)


print(result)





