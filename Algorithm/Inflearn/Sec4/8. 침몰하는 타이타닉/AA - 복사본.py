#%%
import time
st = time.time()
import sys
with open('in5.txt') as sys.stdin:
    n, m = map(int,sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    cnt = s = 0
    e = n-1
    while s <= e:
        if a[s]+a[e] <= m:
            s += 1
        e -= 1
        cnt += 1
    print(cnt)
print(time.time()-st)
        

    
#%%
# solution
import time
st = time.time()
import sys
from collections import deque
with open('in5.txt') as sys.stdin:
    n, limit = map(int,sys.stdin.readline().split())
    p = list(map(int, sys.stdin.readline().split()))
    p.sort()
    p=deque(p)
    cnt=0
    while p:
        if len(p)==1:
            cnt+=1
            break
        if p[0]+p[-1]>limit:
            p.pop()
            cnt+=1
        else:
            p.popleft()
            p.pop()
            cnt+=1
    print(cnt)
print(time.time()-st)


# %%
