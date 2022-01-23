# map을 이용하여 입력값 사칙연산 후 출력

n, m = map(int,input().split())
print(n + m, n - m, n*m, n//m, n%m, sep ='\n')


# 추가 (백준 10340번)

a, b, c = map(int,input().split())
print((a + b)%c, ((a%c) + (b%c))%c, (a*b)%c, ((a%c) * (b%c))%c, sep ='\n')


# BAEKJOON 2588

num1 = int(input())
num2 = input()
for i in range(len(num2),0, -1):
    print(num1 * int(num2[i-1]))
print(num1* int(num2))


# BAEKJOON 1330

n, m = map(int,input().split())
if n > m:
    print('>')
elif n < m:
    print('<')
else:
    print('==')

# BAEKJOON 9498
a = int(input())
if 90 <= a <= 100:
    print('A')
elif 80 <= a < 90:
    print('B')
elif 70 <= a < 80:
    print('C')
elif 60 <= a < 70:
    print('D')
else:
    print('F')


# BAEKJOON 2753
a = int(input())
if a%4 == 0 and (a%100 != 0 or a%400 == 0):
    print('1')
else:
    print('0')


# BAEKJOON 14681

num1 = int(input())
num2 = int(input())

if num1 > 0 and num2 > 0:
    print(1)
elif num1 > 0 and num2 < 0:
    print(4)
elif num2 < 0:
    print(3)
else:
    print(2)


# BAEKJOON 2884
time, minutes = map(int,input().split())
if time == 0:
    if minutes >= 45:
        print(time, minutes-45)
    else:
        print(23, minutes + 15)
elif minutes >= 45:
    print(time, minutes-45)
else:
    print(time -1, minutes + 15)


# BAEKJOON 2739

num1 = int(input())
for i in range(1, 10):
    a = num1 * i
    print('{0} * {1} = {2}'.format(num1, i, a))


# BAEKJOON 10950

num1 = int(input())
for _ in range(num1):
    a, b = map(int, input().split())
    print(a+b)


# BAEKJOON 8393
num1 = int(input())
a = 0
for i in range(1, num1+1):
    a += i
print(a)


# BAEKJOON 15552
import sys
 
num = int(input())
for i in range(num):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)


# BAEKJOON 2741
for i in range(1, int(input())+1):
    print(i)


# BAEKJOON 2742
for i in range(int(input()), 0, -1):
    print(i)



# BAEKJOON 11021
import sys
num = int(input())
for i in range(1, num+1):
        a,b = map(int, sys.stdin.readline().split())
        print('Case #{0}: {1}'.format(i, a+b))


# BAEKJOON 11022
import sys
num = int(input())
for i in range(1, num+1):
        a,b = map(int, sys.stdin.readline().split())
        print('Case #{0}: {1} + {2} = {3}'.format(i, a, b, a+b))


# BAEKJOON 2438
for i in range(1, int(input())+1):
    print('*'*i)


# BAEKJOON 2439
num = int(input())
for i in range(1, num+1):
    a = '*'*i
    print(a.rjust(num))




