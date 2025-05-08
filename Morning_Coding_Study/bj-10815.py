N = int(input())
N_L = set(map(int, input().split()))
M = int(input())
M_L = list(map(int, input().split()))
result = []

for m in M_L:
    if m in N_L:
        result.append('1')
    else:
        result.append('0')

print(' '.join(result))