tall = []
for i in range(9):
    tall.append(int(input()))

# 2개를 뺀 합이 100이면 정답
result = []

for temp1 in range(9): # 1
    for temp2 in range(temp1+1, 9): # 8
        t = tall[:temp1] + tall[temp1+1:temp2] + tall[temp2+1:]
        if sum(t) == 100:
            result.append(t)
            break

result[0].sort()
for temp in range(7):
    print(result[0][temp])