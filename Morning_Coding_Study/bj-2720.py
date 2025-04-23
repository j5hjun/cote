T = int(input())
Q = 25
D = 10
N = 5
P = 1

for t in range(T):
    C = int(input())
    Q_result = C // Q
    Q_c = C % Q
    D_result = Q_c // D
    D_c = Q_c % D
    N_result = D_c // N
    N_c = D_c % N
    P_result = N_c // P
    print(Q_result, D_result, N_result, P_result)