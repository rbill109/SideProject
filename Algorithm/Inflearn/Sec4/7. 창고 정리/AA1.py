import sys
l = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
a.sort()
for _ in range(m):
    min_idx = a.index(min(a))
    max_idx = a.index(max(a))
    a[min_idx] += 1
    a[max_idx] -= 1
print(max(a)-min(a))
