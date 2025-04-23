S = int(input())
i = 1
sum = 0

while sum < S:
    sum += i
    i += 1
    # print(sum)
if sum == S:
    print(i-1)
else:
    print(i-2)