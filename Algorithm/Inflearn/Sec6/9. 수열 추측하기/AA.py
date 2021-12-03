#%%
import sys

def DFS(v, tot):
    if tot > f:
        return
    if v==n and tot==f:
        for i in a:
            print(i, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i] = 1
                a[v] = i
                DFS(v+1, tot+(a[v]*b[v]))
                ch[i] = 0

if __name__ == "__main__":
    # with open('in6.txt') as sys.stdin:
    n, f = map(int, sys.stdin.readline().split())
    a = [0]*n
    b = [1]*n
    ch = [0]*(n+1)
    for i in range(1, n-1):
        b[i] = b[i-1]*(n-i)//i
    DFS(0, 0)


#%%
# solution
# import sys

# def DFS(L, sum):
#     if L==n and sum==f:
#         for x in p:
#             print(x, end=' ')
#         sys.exit(0)
#     else:
#         for i in range(1, n+1):
#             if ch[i]==0:
#                 ch[i]=1
#                 p[L]=i
#                 DFS(L+1, sum+(p[L]*b[L]))
#                 ch[i]=0

# if __name__ == "__main__":
#     n, f = map(int, sys.stdin.readline().split())
#     p=[0]*n
#     b=[1]*n
#     ch=[0]*(n+1)
#     for i in range(1, n):
#         b[i]=b[i-1]*(n-i)//i
#     DFS(0, 0)


#%%
# import sys
# import itertools as it

# n, f = map(int, sys.stdin.readline().split())
# a = list(range(1, n+1))
# b = [1]*n
# cnt = 0
# for i in range(1, n):
#     b[i] = b[i-1]*(n-i)//i
# print(a)
# for tmp in it.permutations(a):
#     print(tmp)
#     sum=0
#     for L, x in enumerate(tmp):
#         sum += (x*b[L])
#     if sum==f:
#         for i in tmp:
#             print(i, end=' ')
#         break


