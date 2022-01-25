# 10952
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a+b)

# 10951
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break