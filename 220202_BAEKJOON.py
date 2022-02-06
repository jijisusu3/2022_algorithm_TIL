# 3052
import sys
lst = [sys.stdin.readline().strip() for i in range(10)]
lst2 = []
for num in lst:
    lst2.append(int(num)%42)
set1 = set(lst2)
print(len(set1))


# 1546
num = int(input())
scores = list(map(int, input().split()))
x = 0
max_score = max(scores)
for i in scores:
    x += (i/max_score)*100
result = x/num
print(result)

