M = int(input())
N = int(input())
L = []
result = []

for i in range(M, N+1):
    for v in range(2, i):
        if i % v == 0:
            if i not in L:
                L.append(i)
    if i not in L:
        result.append(i)

if len(result) != 0:
    print(sum(result))
    print(min(result))
else:
    print(-1)