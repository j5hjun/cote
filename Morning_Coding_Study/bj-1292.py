A, B  = map(int, input().split())

number = 1
result = []

while number < 1001:
    for i in range(number):
        result.append(number)

    number += 1

print(sum(result[A-1:B]))