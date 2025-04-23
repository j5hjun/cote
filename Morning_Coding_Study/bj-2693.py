T = int(input())
for t in range(T):
    L = list(map(int, input().split()))
    L.sort()
    print(L[-3])