N = 4

# 방법 1 : 비트연산자 이용
for subset in range(1 << N): # 중복 피하려면 N-1 넣으면 됨 why?
    A, B = [], []
    for i in range(N):
        if subset & (1 << i):
            A.append(i)
        else:
            B.append(i)
    if len(A) == len(B):
        print(A, B)

# 방법 2 : 백트레킹


def subset(k):
    if k == N:
        if len(A) == len(B):
            print(A, B)
    else:
        A.append(k)
        subset(k + 1)
        A.pop()

        B.append(k)
        subset(k + 1)
        B.pop()


A, B = [], []
subset(0)

# 중복 없애려면?


def subset_2(k):
    if len(A) == N // 2:
        print(A, B + [i for i in range(k, N)])
        return
    if len(B) == N // 2:
        print(A + [i for i in range(k, N)], B)
        return
    if len(A) > N // 2 or len(B) > N // 2:
        print(A, B)
    else:
        A.append(k)
        subset_2(k + 1)
        A.pop()

        B.append(k)
        subset_2(k + 1)
        B.pop()


A, B = [0], []
subset_2(1)