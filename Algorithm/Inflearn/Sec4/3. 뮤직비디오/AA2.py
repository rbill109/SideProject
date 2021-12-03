import sys
N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
lt = 1
rt = sum(a)
# print(a)
while lt <= rt:
    mid = (lt+rt)//2 
    volume = 0
    cnt = 1
    for i in a:
        volume += i
        if volume > mid:
            volume = i
            cnt += 1
    print(f"lt, rt: {lt}, {rt}")
    print(f"최소 용량이 {mid}일 때 총 DVD 개수: {cnt}")
    # DVD 개수가 너무 적어 용량을 줄여야 하는 경우
    # DVD 개수가 M개이지만 최소 용량이 아닌 경우
    if (cnt <= M)&(mid >= max(a)): 
        res = mid
        rt = mid - 1
    # DVD 개수가 너무 많아 용량을 늘려야 하는 경우
    else: 
        lt = mid + 1

print(res)





