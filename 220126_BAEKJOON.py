# 1110

num = int(input())
result = 0
number = num
while True:
    a = num//10   # 10의 자리 숫자
    b = num % 10   # 1의 자리 숫자
    c = (a + b)% 10 # a+b했을 때의 1의 자리 숫자
    num = (b * 10) + c # 원래 1의자리 수를 새로운 숫자의 10의 자리수로~, + c
    result += 1 # 사이클 길이 +1
    if num == number: #원하는 결과가 나오면
        break   #while문을 멈춘다
print(result)