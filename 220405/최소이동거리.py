V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))  # 무향그래프

# D 배열을 생성하고 초기화
D = [0xffffff] * (V + 1)

# 경로를 저장해보자!
P = [0] * (V + 1)  # 부모를 가르키는 트리~

# 시작점을 0으로 설정
D[1] = 0

# # while 활용!
# Q = [1]
#
# while Q:
#     u = Q.pop(0)
#     for v, w in G[u]:
#         if D[v] > D[u] + w:
#             D[v] = D[u] + w
#             P[v] = u
#             Q.append(v)


# # 2
# visited = [0] * (V + 1)
# for _ in range(V):
#     u, min_val = 0, 0xffffff
#     for i in range(1, V + 1):
#         if not visited[i] and min_val > D[i]:
#             u, min_val = i, D[i]
#         visited[u] = 1
#
#         for v, w in G[u]:
#             if not visited[v] and D[u] > D[u] + w:
#                 D[v] = D[u] + w


# # 힙 이용
import heapq
# visited = [0] * (V + 1)
# Q = []
# heappush(Q, (0, 1))
# while Q:
#     w, u = heappop(Q)
#     if visited[u]: continue
#     visited[u] = 1
#     for v, w in G[u]:
#         if not visited[v] and D[v] > D[u] + w:
#             D[v] = D[u] + w
#             heappush(Q, (w, v))
#
#
#
# print(D[1:])