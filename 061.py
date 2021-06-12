Q = int(input())

cards = [0 for _ in range(2*Q)]
front, back = Q, Q

for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        front -= 1
        cards[front] = x
    elif t == 2:
        cards[back] = x
        back += 1
    else:
        print(cards[front+x-1])
