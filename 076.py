import bisect

N = int(input())
A = list(map(int, input().split()))

if sum(A) % 10 != 0:
    print('No')
    exit(0)

tenth = sum(A) // 10

cum = [0] + A*2
for i in range(1, len(cum)):
    cum[i] += cum[i-1]

for i in range(len(cum)):
    index = bisect.bisect_left(cum, cum[i]+tenth)
    if index < len(cum) and cum[index] == cum[i]+tenth:
        print('Yes')
        exit(0)

print('No')
