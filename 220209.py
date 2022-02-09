# BAEKJOON(10989): 수 정렬하기 3

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

for i in range(len(lst)):
    a = len(lst)-i # len(lst)가 10일 때, 9-8-7-6-5-4-3-2-1

