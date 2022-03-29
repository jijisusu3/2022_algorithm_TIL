

def solve(lst3):
    for i in range(len(lst2)):
        dec = 0
        lst2[i] = (lst2[i] + 1)%2
        for idx in range(len(lst2)): # 10진수로 변환함
            dec = dec*2 + lst2[idx]
        s = []
        ret = dec
        while dec > 0:
            s.append(dec%3)
            dec //= 3
        lst3 = lst3[::-1]
        cnt = 0
        for idx in range(min(len(s), len(lst3)):
            if s[idx] != lst3[idx]:
                cnt += 1
            cnt += abs(len(s)-len(lst3))

        if cnt == 1:
            return ret

        lst2[i] = (lst2[i] + 1) % 2


TC = int(input())
for tc in range(1, TC + 1):
    lst2 = list(map(int, input()))
    lst3 = list(map(int, input()))
    ans = solve()
    print(ans)