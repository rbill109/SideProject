#%%
import time
st = time.time()
import sys

def DFS(v):
    global cnt
    if v==n:
        cnt += 1
        # for i in path:
        #     print(i, end=' ')
        # print()
    else:
        for i in range(1, n+1):
            if g[v-1][i-1]==1 and ch[i]==0:
                ch[i]=1
                # path.append(i)
                DFS(i)
                # path.pop()
                ch[i]=0

if __name__=="__main__":
    with open('in5.txt') as sys.stdin:
        n, m = map(int, sys.stdin.readline().split())
        g = [[0]*(n) for _ in range(n)]
        for i in range(m):
            a, b = map(int, sys.stdin.readline().split())
            g[a-1][b-1] = 1
        ch = [0]*(n+1)
        cnt = 0 
        ch[1]=1
        # path = [1]
        DFS(1)
        print(cnt)
    print(time.time()-st)


#%%
# solution
# import sys

# def DFS(v):
#     global cnt, path
#     if v==n:
#         cnt += 1
#         for i in path:
#             print(i, end=' ')
#         print()
#     else:
#         for i in range(1, n+1):
#             if g[v][i]==1 and ch[i]==0:
#                 ch[i]=1
#                 path.append(i)
#                 DFS(i)
#                 path.pop()
#                 ch[i]=0
           
# if __name__=="__main__":
#     n, m = map(int, sys.stdin.readline().split())
#     g=[[0]*(n+1) for _ in range(n+1)]
#     ch=[0]*(n+1)
#     for i in range(m):
#         a, b = map(int, sys.stdin.readline().split())
#         g[a][b]=1
#     cnt=0
#     ch[1]=1
#     path = list()
#     path.append(1)
#     DFS(1)
#     print(cnt)

#%%
import time
st = time.time()
import sys 
def DFS(v):
    global cnt
    if v==n:
        cnt += 1
    else:
        # print(g[v-1])
        for i in g[v-1]:
            if ch[i] == 0:
                ch[i] = 1
                # print(f"visit:{i}")
                DFS(i)
                ch[i] = 0
        # print("for end")
           
if __name__=="__main__":
    with open('in5.txt') as sys.stdin:
        n, m = map(int, sys.stdin.readline().split())
        g = [[] for _ in range(n)]
        for i in range(m):
            a, b = map(int, sys.stdin.readline().split())
            g[a-1].append(b)
        ch = [0]*(n+1)
        cnt = 0 
        ch[1]=1
        # path = [1]
        DFS(1)
        print(cnt)
print(time.time()-st)
# %%
