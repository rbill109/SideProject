import sys
n, m = map(int, sys.stdin.readline().split())
rv = [0]*(n+m)
for i in range(1, n+1):
    for j in range(1, m+1):
        rv[i+j-1] += 1
for idx, i in enumerate(rv):
    if i == max(rv):
        print(idx+1, end=" ")