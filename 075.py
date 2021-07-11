N = int(input())
cnt = 0

for i in range(2, N+1):
    if N == 1:
        break
    if i*i > N:
        cnt += 1
        break
    while N % i == 0:
        cnt += 1
        N //= i

ans = 0
while cnt > 1:
    ans += 1
    cnt = (cnt + 1) // 2

print(ans)
