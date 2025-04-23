N = int(input())

from collections import deque
# 골라서 위 아래 오른쪽 왼쪽 중에 하나가 1이면 이동 후 개수 저장

maps = []

for n in range(N):
    maps.append(list(map(int, input())))

q = deque()
q.append([0,0])
while q:
    # print(q.popleft())
    x, y = q.popleft()
    print(x, y)