#%%
import sys

def DFS(v, tot):
    global cnt
    if tot>T:
        return
    if v==k:
        if tot==T:
            cnt += 1
    else:
        for i in range(a[v][1]+1):
            DFS(v+1, tot+a[v][0]*i)

if __name__ == "__main__":
    # with open('in1.txt') as sys.stdin:
    T = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    a = []
    for _ in range(k):
        p, n = map(int, sys.stdin.readline().split())
        a.append([p, n])
    cnt = 0
    DFS(0, 0)
    print(cnt)


#%%
# solution
# import sys

# def DFS(L, sum):
#     global cnt
#     if sum>m:
#         return
#     if L==n:
#         if sum==m:
#             cnt+=1
#     else:
#         for i in range(cn[L]+1):
#             DFS(L+1, sum+(cv[L]*i))

# with open('in1.txt') as sys.stdin:
#     m = int(sys.stdin.readline())
#     n = int(sys.stdin.readline())
#     cv=list()
#     cn=list()
#     for i in range(n):
#         a, b = map(int, sys.stdin.readline().split())
#         cv.append(a)
#         cn.append(b)
#     cnt=0
#     DFS(0, 0)
#     print(cnt)
# %%
