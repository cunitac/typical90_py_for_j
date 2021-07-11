MOD = 1_000_000_007

N, K = map(int, input().split())

ans = K

if N >= 2:
    ans *= K-1
    ans %= MOD
    ans *= pow(K-2, N-2, MOD)
    ans %= MOD

print(ans)
