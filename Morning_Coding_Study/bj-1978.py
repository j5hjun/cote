N = int(input())
S = list(map(int, input().split()))
result = 0
result_L = []

for i in S:
    if i != 1:
        for t in range(2, i): # 1과 자기자신을 제외한 수를 나눠서 나머지가 0이 이나면
            if i % t != 0:
                result = i
    if result != 0:
        result_L.append(result)

print(len(result_L))
print(result_L)