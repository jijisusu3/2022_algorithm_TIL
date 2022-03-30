import sys;

sys.stdin = open('5203.txt')


def baby_jin(people):
    for x in range(10):
        if people[x] == 3:
            return 1
        if x < 8:
            if people[x] != 0 and people[x + 1] != 0 and people[x + 2] != 0:
                return 1
    return 0


TC = int(input())
for tc in range(1, TC + 1):
    cards = list(map(int, input().split()))
    first = [0] * 10
    second = [0] * 10
    for i in range(12):
        if i % 2 == 0:
            first[cards[i]] += 1
            if i >= 4:
                if baby_jin(first):
                    print(f'#{tc} 1')
                    break
        else:
            second[cards[i]] += 1
            if i > 4:
                if baby_jin(second):
                    print(f'#{tc} 2')
                    break
    else:
        print(f'#{tc} 0')
