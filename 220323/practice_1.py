temp = '0000000111100000011000000111100110000110000111100111100111111001100111'
arr = list(map(int, temp))
for i in range(0, 70, 7):
    ten = 0
    x = arr[i:i+7]
    for j in range(0, 7):
        ten += x[j]*(2**(6-j))
    print(ten, end=' ')