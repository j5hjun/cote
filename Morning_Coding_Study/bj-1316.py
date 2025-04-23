N = int(input())
count = 0

for i in range(N):
    result = []
    word = input()
    for t in range(0,len(word)): # 0부터 3까지 같다 0꺼 추가 4부터 검색색
        if t == len(word)-1:
            if word[t-1] != word[t]:
                result.append(word[t])
        else:
            if word[t] != word[t+1]:
                result.append(word[t])
    dup = []
    for r in result:
        if r not in dup:
            dup.append(r)
    if len(result) == len(dup):
        count += 1
print(count)