import sys
K, N = map(int, sys.stdin.readline().split())
a = [int(sys.stdin.readline().strip()) for _ in range(K)]
lt = 1
rt = max(a)
while lt <= rt:
    mid = (lt+rt)//2
    cnt = sum(map(lambda x: x//mid, a))
    if cnt >= N:
        lt = mid + 1
        res = mid
    else:
        rt = mid - 1 
print(res)
