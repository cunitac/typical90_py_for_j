import math

A, B = map(int, input().split())
gcd = math.gcd(A, B)
lcm = A // gcd * B

if lcm > 1e18:
    print('Large')
else:
    print(lcm)
