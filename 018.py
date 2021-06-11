import math

T = float(input())
L, X, Y = map(float, input().split())
Q = int(input())

for _ in range(Q):
    E = float(input())
    rad = - 2*math.pi * E / T
    y = L/2 * math.sin(rad)
    z = L/2 * (1 - math.cos(rad))

    dist = math.sqrt(X*X + (Y-y)*(Y-y))
    print(math.degrees(math.atan2(z, dist)))
