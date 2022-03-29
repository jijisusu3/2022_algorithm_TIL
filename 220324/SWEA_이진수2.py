TC = int(input())
for tc in range(1, TC + 1):
    N = float(input())
    result = ''
    n = -1
    while N > 0:
        result += str(int(N//2**n))
        N %= 2**n
        n -= 1
        if n < -13:
            break

    if len(result) > 12:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {result}')
