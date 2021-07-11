N, M = map(int, input().split())
count = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    if a < b:
        count[b-1] += 1
    else:
        count[a-1] += 1
print(sum(1 for i in range(N) if count[i] == 1))
