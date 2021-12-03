#%%
import sys

def DFS(v):
    global cnt
    if v==m:
        for i in a:
            print(a[i], end=" ")
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if check[i] == 0:
                check[i] = 1
                a[v] = i
                DFS(v+1)
                check[i] = 0

if __name__=="__main__":
    n, m = map(int, sys.stdin.readline().split())
    a = [0]*m
    check = [0]*(n+1)
    cnt = 0
    DFS(0)
    print(cnt)
#%%




# solution
# import sys

# def DFS(L):
#     global cnt
#     if L==m:
#         for i in range(m):
#             print(res[i], end=' ')
#         print()
#         cnt+=1
#     else:
#         for i in range(1, n+1):
#             if ch[i]==0:
#                 ch[i]=1
#                 res[L]=i
#                 DFS(L+1)
#                 ch[i]=0

# if __name__=="__main__":
#     n, m = map(int, sys.stdin.readline().split())
#     res=[0]*n
#     ch=[0]*(n+1)
#     cnt=0
#     DFS(0)
#     print(cnt)