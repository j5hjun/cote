N = int(input())

# 9876543210
# 0~10
# 20 21 30 31 32
# 첫째자리보다 둘째자리가 더 커야함
# 같은 숫자는 나올 수 없음

L = [0,1,2,3,4,5,6,7,8,9]
for l in L:
    for t in range(int(str(l)[-1])):
        L.append(l*10+t)
    if len(L) == N:
        break
print(L[N])