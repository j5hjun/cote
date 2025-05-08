from collections import deque

N, K = map(int, input().split())

q = deque()
for i in range(N):
    q.append(list(map(int, input().split())))

