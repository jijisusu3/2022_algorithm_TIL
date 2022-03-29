import sys
sys.stdin = open('1240.txt')

TC = int(input())

dictionary = {
    '0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3',
    '0100011': '4', '0110001': '5', '0101111': '6', '0111011': '7',
    '0110111': '8', '0001011': '9'
}

for tc in range(1, TC + 1):
    result = []
    N, M = map(int, input().split())
    lst = [input() for _ in range(N)]
    arr = '' # 바코드 있는 줄 일단 담기
    for i in lst:
        if '1' in i:
            arr = i
            break


    # 다 맨 뒤가 1이니까 가장 뒤에 있는 1 찾아서 password 추출

    password = []
    for i in range(M - 1, -1, -1):
        if '1' == arr[i]:
            password = arr[i - 55:i + 1]
            break

    standard = 0
    odd = 0
    even = 0
    for j in range(0, 56, 7):
        standard += 1
        if standard % 2 == 1: # 홀수일 때
            odd += int(dictionary[password[j:j+7]])
        else:
            if standard != 8: # 검증코드 아닐 때 -> 짝수일 때
                even += int(dictionary[password[j:j+7]])
            else: # 검증코드일 때
                temp_num = ((odd * 3) + even + int(dictionary[password[j:j + 7]]))
                if temp_num % 10 == 0:
                    print(f'#{tc} {odd + even + int(dictionary[password[j:j + 7]])}')
                else:
                    print(f'#{tc} {0}')