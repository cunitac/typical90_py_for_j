N = int(input())
A = [int(s) for s in input().split()]
Q = int(input())
B = [int(input()) for _ in range(Q)]

A.sort()

for b in B:
    left, right = 0, N-1
    while left+1 < right:
        mid = (left + right) // 2
        if b < A[mid]:
            right = mid
        else:
            left = mid
    print(min(abs(A[left]-b), abs(A[right]-b)))
