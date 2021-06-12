MOD = int(1e9+7)

N = int(input())
As = [list(map(int, input().split())) for _ in range(N)]

S = 1
for A in As:
    S = sum(a * S for a in A) % MOD

print(S)
