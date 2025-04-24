dot = [4]
m = 2

for i in range(15):
    m = 2*m - 1
    dot.append(m*m)

N = int(input())
print(dot[N])