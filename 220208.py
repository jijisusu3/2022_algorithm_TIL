
# code-up (3321) : 최고의 피자

topping_num = int(input()) # 토핑의 수
dough_price, topping_price = map(int, input().split()) # 공백으로 나누어서 도우 가격과, 토핑 하나 당 가격 받아오기
dough_calorie = int(input()) # 도우의 칼로리
toppings = [] # 토핑 칼로리들 저장할 빈 리스트
for _ in range(topping_num): # 토핑의 수 만큼
    toppings.append(int(input())) # 토핑의 칼로리를 입력받아, 빈 리스트에 하나하나 채워넣는다. 
toppings.sort(reverse=True) # 칼로리 높은 것 부터 받기 위해 sort(reverse=True)를 통해 내림차순으로 정리한다.

result = 0 # print할 값
t_kcal = 0 # 토핑들의 칼로리를 더할 값
t_cost = 0 # 토핑들의 가격을 더할 값
for i in toppings: # 내림차순으로 정렬된 토핑칼로리 리스트를 돌면서
    t_kcal += i # 토핑 칼로리를 더하고
    t_cost += topping_price # 토핑 가격도 더하고 
    total = (dough_calorie + t_kcal)/(dough_price+t_cost)  #1달러 당 가격
    if result > total: # total이 result보다 1달러당 가격이 작으면
        break # 반복문 멈추기! 왜냐하면 토핑의 값이 같기 때문에, 내림차순이라 뒤에는 더 낮은 가격의 토핑만 있어서 더 더할 수록 손해임
    else:
        result = total # total이 result보다 1달러당 가격이 크면, 그 값을 다음 반복문에서 비교해봐야하니까 result에 넣기
print(int(result))



