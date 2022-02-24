import sys;

sys.stdin = open('4880.txt')


# 1은 가위, 2는 바위, 3은 보


def playgame(left_index, right_index):
    l, r = cards[left_index - 1], cards[right_index - 1]
    if l == r:
        return left_index
    elif l == 1:  # 가위
        if r == 3:
            return left_index
        elif r == 2:
            return right_index
    elif l == 2:  # 바위
        if r == 1:
            return left_index
        elif r == 3:
            return right_index
    elif l == 3:  # 보
        if r == 2:
            return left_index
        elif r == 1:
            return right_index


def findmin(start, end):
    if start == end:
        return start
    else:
        mid = (start + end) // 2
        left = findmin(start, mid)
        right = findmin(mid + 1, end)
        return playgame(left, right)


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    result = findmin(1, N)
    print(f'#{tc} {result}')
