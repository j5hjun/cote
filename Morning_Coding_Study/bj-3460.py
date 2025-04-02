T = int(input())

j = 0
answer_L = []

for i in range(T):
    L = []
    n = int(input())
    while n > 0:
        if (n / (2**j)) < 1:
            n -= 2**(j-1)
            L.append(str(j-1))
            j = 0
        elif (n / (2**j)) == 1:
            n -= 2**j
            L.append(str(j))
            j = 0
        
        j += 1

    answer = ""
    for t in range(len(L)-1 , -1, -1):
        if t == 0:
            answer += L[t]
        else:
            answer += L[t] + " "
    answer_L.append(answer)

for al in answer_L:
    print(al)
