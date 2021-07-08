import numpy as np

N, K = input().split()
N, K = int(N, 8), int(K)

for _ in range(K):
    N = np.base_repr(N, 9)
    N = N.replace('8', '5')
    N = int(N, 8)

print(np.base_repr(N, 8))
