N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

Am = [0 for _ in range(46)]
Bm = [0 for _ in range(46)]
Cm = [0 for _ in range(46)]

for i in range(N):
    Am[A[i] % 46] += 1
    Bm[B[i] % 46] += 1
    Cm[C[i] % 46] += 1

ans = 0

for m0 in range(46):
    for m1 in range(46):
        for m2 in range(46):
            if (m0+m1+m2) % 46 == 0:
                ans += Am[m0]*Bm[m1]*Cm[m2]

print(ans)
