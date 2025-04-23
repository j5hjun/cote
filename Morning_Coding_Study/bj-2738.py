N, M = map(int, input().split())
H1 = []
H2 = []
H = []

for m1 in range(M):
    H1.append(list(map(int, input().split())))
for m2 in range(M):
    H2.append(list(map(int, input().split())))

for m in range(M):
    for n in range(N):
        H.append(H1[m][n] + H2[m][n])

print(H)