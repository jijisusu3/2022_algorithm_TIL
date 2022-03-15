# 1
new_id = input().lower()
# 2
answer = ''
for i in new_id:
    if not i in '~!@#$%^&*()=+[{]}:?,<>/':
        answer += i
# 3
while '..' in answer:
    answer = answer.replace('..', '.')
# 4
if answer[0] == '.':
    answer = answer[1:]
if answer[-1] == '.':
    answer = answer[:-1]
# 5
answer = 'a' if answer == '' else answer
# 6
if len(answer) > 15:
    answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
# 7
if len(answer) <= 2:
    while len(answer) > 2:
        answer += answer[-1]

print(answer)
