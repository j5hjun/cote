NP = input()
# NP = "25 4"
N = int(NP.split()[0])
P = int(NP.split()[1])
L = []
for t in range(1, N+1):
    if N%t == 0:
        L.append(t)
if len(L) < P:
    print(0)
else:
    print(L[P-1])