from collections import deque
import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
L = deque()

for i in range(N):
    C = data[i + 1].split()
    if C[0] == 'push':
        L.append(int(C[1]))
    elif C[0] == 'pop':
        if len(L) != 0:
            print(L.popleft())
        else:
            print(-1)
    elif C[0] == 'size':
        print(len(L))
    elif C[0] == 'empty':
        if len(L) != 0:
            print(0)
        else:
            print(1)
    elif C[0] == 'front':
        if len(L) != 0:
            print(L[0])
        else:
            print(-1)
    elif C[0] == 'back':
        if len(L) != 0:
            print(L[-1])
        else:
            print(-1)