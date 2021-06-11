H, W = (int(s) for s in input().split())
A = [[int(s) for s in input().split()] for _ in range(H)]

sum_row = [sum(A[i][j] for j in range(W)) for i in range(H)]
sum_col = [sum(A[i][j] for i in range(H)) for j in range(W)]

for i in range(H):
    res_row = (sum_row[i] + sum_col[j] - A[i][j] for j in range(W))
    print(' '.join(str(r) for r in res_row))
