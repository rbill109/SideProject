import sys
n = int(sys.stdin.readline())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
a.sort(key=lambda x : (x[1], x[0]))
e = cnt = 0
for m in a:
    if m[0] >= e:
        e = m[1]
        cnt += 1
print(cnt)