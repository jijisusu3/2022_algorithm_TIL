memo = [-1]*13


def dfs(n, ssum):
    global ans
    if n > 12:
        if ans > ssum:
            ans = ssum
        return 0
    if memo[n] != -1:
        return memo[n]
    else:
        if lst[n] == 0:
            dfs(n + 1, ssum)
        else:
            dfs(n + 1,  ssum + lst[n] * day)
            dfs(n + 1, ssum + mon)
            dfs(n + 3, ssum + mon3)


TC = int(input())
for tc in range(1, TC + 1):
    day, mon, mon3, year = map(int, input().split())
    lst = [0] + lst(map(int, input().split()))
    ans = year
    dfs(1, 0)
    print(ans)