N, M = map(int, input().split())
graph = []
coin1 = []
coin2 = []

for i in range(N):
    line = list(map(str, input()))
    if 'o' in line:
        if coin1:
            coin2 = [line.index('o'), i]
        else:
            coin1 = [line.index('o'), i]

    graph.append(line)
print(graph)

d = [[-1,0], [1, 0], [0, 1], [0, -1]]
q = [[0,0]]

while q:
    x, y = q.pop(0)

    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]

        