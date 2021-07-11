MOD = 1_000_000_007

L, R = map(int, input().split())

ans = 0

for n_digit in range(1, 20):
    ll = pow(10, n_digit-1)
    rr = pow(10, n_digit)
    l = min(rr, max(ll, L))
    r = min(rr, max(ll, R+1))
    cnt = (l+r-1) * (r-l) // 2
    ans += cnt * n_digit
    ans %= MOD

print(ans)
