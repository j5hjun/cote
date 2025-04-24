from collections import deque

N, M, K = map(int, input().split())
ft = deque()

for k in range(K):
    ft.append(list(map(int, input().split())))

count = 1

while ft:
    r, c = ft.popleft()
    if [r+1, c] in ft:
        count