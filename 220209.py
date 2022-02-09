# # BAEKJOON(10989): 수 정렬하기 3

# # Bubble Sort -> 백준에서는 메모리 초과 뜸
# import sys
# n = int(input())
# lst = []
# for _ in range(n):
#     lst.append(int(sys.stdin.readline()))
# for i in range(n-1, 0, -1):
#     for j in range(0, i):
#         if lst[j] > lst[j+1]:
#             lst[j], lst[j+1] = lst[j+1], lst[j]
# print(*lst, sep='\n')

# # Counting Sort
# import sys
# n = int(sys.stdin.readline())
# lst = [0]*10001
# for _ in range(n):
#     num = int(sys.stdin.readline())
#     lst[num] += 1
#
# for i in range(1, 10001):
#     count = lst[i]
#     for _ in range(count):
#         print(i)




# # code up(3301): 거스름돈

# change = int(input())
# num = 0
# money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

# for i in money :
#     num += change//i
#     change = change%i

# print(num)



# # BAEKJOON(1427): 소트인사이드

# # Counting Sort  -> 백준 사이트에서 안됨... 왜 안되는지 너무 궁금
# num = input()
# temp_lst = [0]*10
# for i in num:
#     temp_lst[int(i)] += 1
# for j in range(len(temp_lst)-1, 0, -1):
#     for _ in range(temp_lst[j]):
#         print(j, end='')


# # 2. 그냥 풀기

# num = input()
# for i in range(9,-1,-1):
#     for j in num:
#         if int(j) == i:
#             print(i, end='')