# BAEKJOON(1543): 문서 검색

doc = list(input())
search = list(input())
x = len(doc)-len(search)
y = len(search)
cnt = 0
i = 0
while i <= x:
    if doc[i:i+y] == search:
        cnt += 1
        i += y
    else:
        i += 1
print(cnt)

