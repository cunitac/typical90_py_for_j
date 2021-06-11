N = int(input())
seen = set()

for i in range(N):
    S = input()
    if S not in seen:
        seen.add(S)
        print(i+1)
