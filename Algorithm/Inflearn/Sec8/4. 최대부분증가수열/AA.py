#%%
import time
st = time.time()
import sys 

if __name__ == "__main__":
    with open('in6.txt') as sys.stdin:
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        dy = [1]*n
        res = 1
        for i in range(1, n):
            len = 0
            for j in range(i-1, 0, -1):
                if a[j]<a[i]:
                    if dy[j]>len:
                        len = dy[j]
            dy[i] = len+1
            if dy[i] > res:
                res = dy[i]
        print(res)
print(time.time()-st)
# %%
import time
st = time.time()
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.insert(0,0)
    dy = [0]*(n+1)
    dy[1] = 1
    res = 0
    for i in range(2, n+1):
        max = 0
        for j in range(i-1, 0, -1):
            if arr[j]<arr[i] and dy[j]>max:
                max = dy[j]
        dy[i] = max+1
        if dy[i]>res:
            res = dy[i]
    print(res)
    
print(time.time()-st)
# %%
# a = list(range(8))
# print(a)
# for i in range(7, 0, -1):
#     print(a[i])
# print()
# for i in a[6:0:-1]:
#     print(i)
# %%
