N = int(input())
M = int(input())

from collections import deque
q = deque()
for i in range(M):
    q.append(list(map(int, input().split())))
start, end = map(int, input().split())

O = 0
for temp in range(M):
    O += temp

result = []
S = start
count = 0
for o in range(O):
    line = q.popleft()
    if line[0] == S:
        if line[1] == end:
            count += line[2]
            result.append(count)
        else:
            S = line[1]
            count += line[2]
            print(line, count)
    else:
        q.append(line)
print(result)