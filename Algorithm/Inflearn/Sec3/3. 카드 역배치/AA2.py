import sys
card = list(range(21))
for _ in range(10):
    s, e = map(int, sys.stdin.readline().split())
    card[s:e+1] = card[s:e+1][::-1]
print(*card[1:], sep= " ")