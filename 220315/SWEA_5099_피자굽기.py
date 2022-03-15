TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    lst = list(map(int,input().split()))
    temp = []
    for i in range(0, len(lst)):
        temp.append((i + 1, lst[i])) #피자 번호랑 치즈 양 함께 저장해둠
    oven_pizza = temp[:N]
    left_pizza = temp[N:]
    while len(oven_pizza) != 1:
        num, cheese = oven_pizza.pop(0)
        cheese_2 = cheese // 2
        if cheese_2 != 0:
            oven_pizza.append((num, cheese_2))
        elif len(left_pizza) > 0:
            oven_pizza.append(left_pizza.pop(0))
    print(f'#{tc} {oven_pizza[0][0]}')
