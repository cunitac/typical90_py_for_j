N = int(input())
S = input()

ans = N * (N+1) // 2
cnt = 1
for i in range(1, len(S)):
    if S[i] == S[i-1]:
        cnt += 1
    else:
        ans -= cnt * (cnt+1) // 2
        cnt = 1
ans -= cnt * (cnt+1) // 2

print(ans)
