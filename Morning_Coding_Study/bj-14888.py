# 답안 1

N = int(input())
numbers = list(map(int, input().split()))
cal_input = list(map(int, input().split()))

max_result = -float('inf')
min_result = float('inf')

q = [(numbers[0], 1, tuple(cal_input))]

while q:
    current, idx, (plus, minus, mul, div) = q[0]
    q = q[1:]

    if idx == N:
        max_result = max(max_result, current)
        min_result = min(min_result, current)
        continue

    num = numbers[idx]
    
    if plus:
        q.append((current + num, idx + 1, (plus-1, minus, mul, div)))
    if minus:
        q.append((current - num, idx + 1, (plus, minus-1, mul, div)))
    if mul:
        q.append((current * num, idx + 1, (plus, minus, mul-1, div)))
    if div:
        if current < 0:
            q.append((-(abs(current) // num), idx + 1, (plus, minus, mul, div-1)))
        else:
            q.append((current // num, idx + 1, (plus, minus, mul, div-1)))

print(max_result)
print(min_result)