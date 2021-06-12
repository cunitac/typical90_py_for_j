N, Q = map(int, input().split())
A = list(map(int, input().split()))

shift = 0

for _ in range(Q):
    T, x, y = map(int, input().split())
    if T == 1:
        x, y = (shift+x-1) % N, (shift+y-1) % N
        A[x], A[y] = A[y], A[x]
    elif T == 2:
        shift -= 1
    else:
        print(A[(shift+x-1) % N])
