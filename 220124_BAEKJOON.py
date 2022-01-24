# BAEKJOON 10871
a = ''
numbers, standard = map(int,input().split())
x = list(input().split())
for i in x:
    i = int(i)
    if i < standard:
        a += str(i)
        a += ' '
print(a)

