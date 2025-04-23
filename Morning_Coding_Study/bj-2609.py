N1, N2 = map(int, input().split())
N1_L = []
MAX = []
MIN = []

for i in range(1, N1+1):
    if N1 % i == 0:
        N1_L.append(i)

for i in range(1, N2+1):
    if N2 % i == 0:
        if i in N1_L:
            MAX.append(i)

print(max(MAX))

while True:
    for i in range(N1+1, 1, -1): # 어떻게 해야하지
        if N1 % i == 0 and N2 % i == 0:
            MIN.append(i)
            N1 //= i
            N2 //= i
            break
    break

sum = 1
for i in MIN:
    sum *= i
print(sum)