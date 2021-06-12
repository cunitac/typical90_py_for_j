N, Q = map(int, input().split())
A = list(map(int, input().split()))

diff = [A[i+1]-A[i] for i in range(N-1)]
inconvinience = sum(abs(d) for d in diff)


for _ in range(Q):
    L, R, V = map(int, input().split())
    if L > 1:
        inconvinience -= abs(diff[L-2])
        diff[L-2] += V
        inconvinience += abs(diff[L-2])
    if R < N:
        inconvinience -= abs(diff[R-1])
        diff[R-1] -= V
        inconvinience += abs(diff[R-1])
    print(inconvinience)
