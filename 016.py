N = int(input())
A, B, C = map(int, input().split())

ans = 9999

for a in range(10000):
    for b in range(10000-a):
        done = a*A + b*B
        if done <= N and (N - done) % C == 0:
            ans = min(ans, a + b + (N - done) // C)

print(ans)
