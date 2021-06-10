N = int(input())

for num in reversed(range(0, 1 << N, 2)):
    bits = list(bin(num)[2:].zfill(N))
    if bits.count('1') != bits.count('0'):
        continue
    i, j = -1, -1
    try:
        for _ in range(N // 2):
            i = bits.index('1', i + 1)
            j = bits.index('0', i + 1)
            bits[i] = ' '
            bits[j] = ' '
    except ValueError:
        continue
    bits = bin(num)[2:].zfill(N)
    result = ''.join('(' if b == '1' else ')' for b in bits)
    print(result)
