N, K = map(int, input().split())
A = [int(s) for s in input().split()]
B = [int(s) for s in input().split()]

diff = sum(abs(A[i]-B[i]) for i in range(N))

if diff <= K and diff % 2 == K % 2:
    print('Yes')
else:
    print('No')
