N = len(board)
answer = 0
lst = []
for col in moves:
    sr = -1
    while sr < N - 1:
        sr += 1
        if board[sr][col-1] != 0:
            if len(lst) == 0 or lst[-1] != board[sr][col-1]:
                lst.append(board[sr][col-1])
                board[sr][col - 1] = 0
            elif lst[-1] == board[sr][col-1]:
                answer += 2
                lst.pop()
                board[sr][col-1] = 0
            break

print(answer)