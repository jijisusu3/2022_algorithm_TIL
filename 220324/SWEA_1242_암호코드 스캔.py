import sys
sys.stdin = open('1242.txt')

dictionary = {
    '0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3',
    '0100011': '4', '0110001': '5', '0101111': '6', '0111011': '7',
    '0110111': '8', '0001011': '9'
}

TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    arr = list(set(arr))

    password = []
    temp = ''
    for line in arr:

    print(arr)
    print()