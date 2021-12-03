import sys
L = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
a.sort()
for _ in range(M):
    a[0], a[-1] = a[0]+1, a[-1]-1
    a.sort()
print(a[-1]-a[0])
