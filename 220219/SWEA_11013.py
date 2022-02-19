import sys ; sys.stdin = open('11013.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 21
    for i in range(N-2): # 첫번째 자르는 애 올 수 있는 정도
        temp1 = arr[:i+1]
        lst1 = sum(temp1)
        for j in range(i+1, N-1): # 두번째 자르는 애가 올 수 있는 정도
            temp2 = arr[i+1:j+1]
            lst2 = sum(temp2)
            temp3 = arr[j+1:]
            lst3 = sum(temp3)
            temp = [lst1, lst2, lst3]
            diff = abs(max(temp)-min(temp))
            if result > diff:
                result = diff
    print(f'#{tc} {result}')



