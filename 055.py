N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

for i0 in range(N):
    for i1 in range(i0+1, N):
        for i2 in range(i1+1, N):
            for i3 in range(i2+1, N):
                for i4 in range(i3+1, N):
                    prod = A[i0] * A[i1]
                    prod %= P
                    prod *= A[i2]
                    prod %= P
                    prod *= A[i3]
                    prod %= P
                    prod *= A[i4]
                    if prod % P == Q:
                        ans += 1

print(ans)
