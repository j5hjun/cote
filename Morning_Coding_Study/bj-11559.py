board = [[],[],[],[],[],[]]

for i in range(12):
    a,b,c,d,e,f = map(str, input().split())
    board[0].append(a)
    board[1].append(b)
    board[2].append(c)
    board[3].append(d)
    board[4].append(e)
    board[5].append(f)

# 4개 이상 모인 것 찾고 없애고 카운트 1
# 없앤만큼 위에 . 추가

for t in range(6):
    board[t]