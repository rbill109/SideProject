import sys
N = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# print(a)
# a.sort(key=lambda x : (x[0], x[1]))
# a.sort(key=lambda x : x[1])
a.sort(key=lambda x : (x[1], x[0]))
# print(a)
cnt = end = 0
for i in a:
    if i[0] >= end:
        cnt += 1
        end = i[1]
    # print(i, cnt)
print(cnt)

