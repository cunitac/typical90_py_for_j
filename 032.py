INF = int(1e9)

N = int(input())
A = [[int(s) for s in input().split()] for _ in range(N)]
M = int(input())

ok = [[True for _ in range(N)] for _ in range(N)]
for _ in range(M):
    X, Y = map(int, input().split())
    ok[X-1][Y-1] = False
    ok[Y-1][X-1] = False


def rec(now, time, i, done):
    if i == N-1:
        return time+A[now][i]

    ret = INF
    done[now] = True
    for next in range(N):
        if not done[next] and ok[now][next]:
            ret = min(ret, rec(next, time+A[now][i], i+1, done))
    done[now] = False
    return ret


done = [False for _ in range(N)]
ans = min(rec(first, 0, 0, done) for first in range(N))

if ans == INF:
    print('-1')
else:
    print(ans)
