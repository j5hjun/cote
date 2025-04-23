N = int(input())
board = []

# 연속된 알파벳의 개수가 N개이면 바로 N 출력

# 0,0 부터 오른쪽과 아래쪽과 교환
# 연속된 알파벳의 개수를 담는다
# 최대 개수를 뽑아서 담는다
# 최대 개수를 출력한다

for i in range(N):
    board.append(list(map(str,input())))

for i in range(N): # 행
    for j in range(N): # 열
        if j + 1 < N:
            board[i][j] = board[i][j+1]
            board[i][j+1] = board[i][j]
            # 행 열 검사
            