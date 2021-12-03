# import sys

# def DFS(v):
#     global cnt
#     print(a)
#     if v==m:
#         for i in range(n):
#             if a[i]!=0:
#                 print(a[i], end=" ")
#         print()
#         cnt += 1    
#     else:
#         for i in range(1,n+1):
#             a[v] = i
#             DFS(v+1)


# if __name__=="__main__":
#     # with open('in1.txt') as sys.stdin:
#     n, m = map(int, sys.stdin.readline().split())
#     a = [0]*(n+1)
#     cnt = 0
#     DFS(0)
#     print(cnt)




#%%
# solution
import sys

def DFS(v):
    global cnt
    if v==m:
        for i in range(m):
            print(a[i], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1, n+1):
            a[v]=i
            DFS(v+1)

           
if __name__=="__main__":
    n, m = map(int, sys.stdin.readline().split())
    a = [0]*m
    cnt=0
    DFS(0)
    print(cnt)


# %%
