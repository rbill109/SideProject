import sys
n, k = map(int, sys.stdin.readline().split())
idx = 0
for i in range(1,n+1):
    if n % i == 0:
        idx += 1
        if idx == k:
            print(i)
if idx < k:
    print(-1)