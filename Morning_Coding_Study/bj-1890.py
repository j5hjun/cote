N = int(input())
board = []

for n in range(N):
    board.append(list(map(int, input().split())))

from collections import deque

q = deque()
q.append((0,0))
count = 0

while q:
    i, j = q.popleft()

    number = board[j][i]

    if i == N-1 and j == N-1:
        count += 1

    else:
        if i+number <= N-1:
            q.append((i+number, j))
        if j+number <= N-1:
            q.append((i, j+number))

print(count)

# 0,0 2,0 2,3 3,3