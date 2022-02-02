# 10818

n = int(input())
lst_num = list(map(int, input().split()))
max_num = lst_num[0]
min_num = lst_num[0]
for i in range(1, n):
    if max_num < lst_num[i]:
        max_num = lst_num[i]
for i in range(1, n):
    if min_num > lst_num[i]:
        min_num = lst_num[i]   
print(min_num,max_num)


# 2562
max_num = int(input())
numbering = 1
for i in range(2,10):
    num_n = int(input())
    if max_num < num_n:
        max_num = num_n
        numbering = i
print(max_num, '/n', numbering)


# 2577
import sys
a, b, c = list(int(sys.stdin.readline()) for _ in range(3)) 
number = str(a*b*c)
result = [0]*10
for i in number:
    result[int(i)] += 1
for i in result:
    print(i)

