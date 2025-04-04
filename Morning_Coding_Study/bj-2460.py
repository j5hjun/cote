sum = 0
L = []

for i in range(10):
    D, U = map(int, input().split())
    sum += -D + U
    if sum >= 10000:
        sum = 10000
    L.append(sum)
print(max(L))