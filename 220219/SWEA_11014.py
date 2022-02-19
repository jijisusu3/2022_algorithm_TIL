import sys ; sys.stdin = open('11014.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split)) for _ in range(N)]
    for r in range(1, N-1):
        for c in range(1, N-1):

            # 세로 덩어리