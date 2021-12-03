#%%
import sys

def DFS(v, tot):
    global cnt
    if tot > m:
        return
    if v >= cnt:
        return
    if tot == m:
        if v < cnt:
            cnt = v
    else:
        for i in a:
            DFS(v+1, tot+i)

if __name__=="__main__":
    # with open('in1.txt') as sys.stdin:
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort(reverse=True)
    m = int(sys.stdin.readline())
    cnt = 2147000000
    DFS(0, 0)
    print(cnt)

#%%

# solution
# import sys

# def DFS(L, sum):
#     global res
#     if L>=res:
#         return
#     if sum>m:
#         return
#     if sum==m:
#         if L<res:
#             res=L
#     else:
#         for i in range(n):
#             DFS(L+1, sum+a[i])

# if __name__=="__main__":
#     n = int(sys.stdin.readline())
#     a = list(map(int, sys.stdin.readline().split()))
#     m = int(sys.stdin.readline())
#     res=2147000000
#     a.sort(reverse=True)
#     DFS(0, 0)
#     print(res)