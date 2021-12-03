#%%
import sys

def DFS(v, s, tot):
    # print(f"\nvisit:{v}")
    global cnt
    if v==k:
        if tot%m==0:
            cnt+=1
    else:
        for i in range(s, n):
                DFS(v+1, i+1, tot+a[i])


if __name__=="__main__":
    # with open('in1.txt') as sys.stdin:
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    cnt=0
    DFS(0, 0, 0)
    print(cnt)

# %%
import sys
import itertools as it

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
cnt=0
for x in it.combinations(a, k):
    if sum(x)%m == 0:
        cnt += 1
print(cnt)