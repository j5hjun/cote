H, W = map(int, input().split())
Q = list(map(int, input().split()))
# 3 1 2 3 4 1 1 2
# 각 층마다 검정색이 양쪽에 있으면 사이의 하얀색의 개수를 합한다
# 검정색 왼쪽 끝부터 오른쪽 끝까지 칸 모두 더하고 검정색만 빼기

sum = 0
max_H = max(Q)
q = Q.copy()

for h in range(1, max_H + 1):
    left_check = 0
    right_check = 0
    i = 0

    while i < W:
        left = q[i]
        right = q[-1-i]
        if left_check == 0:
            if left >= h:
                left_check = 1
                start = i #0

        if right_check == 0:
            if right >= h:
                right_check = 1
                end = W - i - 1 #-1 > 8, -3 > 6 --> x = W - i - 1
        i += 1
    # print(start, end)
    for q2 in q[start : end+1]:
        if q2 < h: # 안채워져 있는 부분
            sum += 1
            # print(q2)
print(sum)