import sys ; sys.stdin = open('5201.txt')

TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split()) # 컨테이너 수, 트럭 수
    containers = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())), reverse=True)
    result = 0
    x = 0
    for i in range(len(trucks)):
        for j in range(x, len(containers)):
            if trucks[i] >= containers[j]:
                result += containers[j]
                x = j + 1
                break
    print(f'#{tc} {result}')
