N = int(input())
A = [int(s) for s in input().split()]
B = [int(s) for s in input().split()]

A.sort()
B.sort()

print(sum(abs(A[i]-B[i]) for i in range(N)))
