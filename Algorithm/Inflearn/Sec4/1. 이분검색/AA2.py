import sys
N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
lt = 0
rt = N
while lt <= rt:
    mid = (lt + rt)//2
    if a[mid] == M: 
        print(mid+1)
        break
    elif a[mid] < M:
        lt += 1
    else:
        rt -= 1

