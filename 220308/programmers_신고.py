id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi", "frodo neo"]
k = 2
id_len = len(id_list)
report = set(report)
report = list(report)

dic = {}

for name in id_list:
    dic[name] = {
        'complain': [],
        'num': 0,
    }

for i in report:
    good, bad = i.split()
    if bad not in dic[name]['complain']:
        dic[good]['complain'].append(bad) # 신고자에게 신고한 사람 기록
        dic['bad']['num'] += 1
    if dic[name]["num"] == k:



ban = []
for x in range(id_len):
    if com_lst[x] >= k:
        ban.append(id_list[x])


for i in range(len(report)):
    good, bad = report[i].split()
    if bad in ban:
        for j in range(id_len):
            if good == id_list[j]:
                letter_list[j] += 1

print(letter_list)
