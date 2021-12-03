import sys
n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
cnt = 0
for i in range(n):
    sum = 0
    for j in range(i,n):
        sum += a[j]
        if sum >= m:
            break
    if sum == m:
        cnt += 1

print(cnt)
