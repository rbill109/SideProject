import sys
a = list(range(1,21))
for _ in range(10):
    s, e = map(int, sys.stdin.readline().split())
    # a[s-1:e] = a[s-1:e][::-1]
    for i in range((e-s+1)//2):
        a[s+i-1], a[e-i-1] = a[e-i-1], a[s+i-1]
print(*a, sep=" ")