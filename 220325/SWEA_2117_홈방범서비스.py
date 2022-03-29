import sys
sys.stdin = open('2117.txt')

TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    d1 = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 상하좌우
    d2 = [(-1, -1), (1, -1), (1, 1), (-1, 1)]  # 대각선
    print(arr)