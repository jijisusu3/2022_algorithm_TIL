# 팩토리얼
a = int(input())
def factorial(a):
    if a < 2:
        return 1
    else:
        return a*factorial(a-1)
print(factorial(a))



# # 피보나치

a = int(input())
def fibo(a):
    if a < 1:
        return 0
    elif a < 2:
        return 1
    else:
        return fibo(a-1) + fibo(a-2)

print(fibo(a))



#하노이 탑

def hanoi(n, a = 1, b = 3):
    if n > 1 :
        hanoi(n-1, a, 6-a-b)
    print(a, b)
    if n > 1:
        hanoi(n-1, 6-a-b, b)

n = int(input())
print(2**n -1)
hanoi(n)