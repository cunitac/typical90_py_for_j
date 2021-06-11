N = int(input())

A = [0 for _ in range(N)]
B = [0 for _ in range(N)]

for i in range(N):
    C, P = map(int, input().split())
    if C == 1:
        A[i] = P
    else:
        B[i] = P

A_cumsum = [0] + A
B_cumsum = [0] + B

for i in range(N):
    A_cumsum[i+1] += A_cumsum[i]
    B_cumsum[i+1] += B_cumsum[i]

Q = int(input())

for _ in range(Q):
    L, R = map(int, input().split())
    print(
        A_cumsum[R] - A_cumsum[L-1],
        B_cumsum[R] - B_cumsum[L-1],
    )
