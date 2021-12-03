# #%%
# import sys
# from collections import deque

# def BFS(n):
#     dQ = deque()
#     dQ.append((0, 0))
#     turn = 0
#     while dQ:
#         tmp = dQ.popleft()
#         for i in range(4):
#             x = tmp[0]+dx[i]
#             y = tmp[1]+dy[i]
#             if 0<=x<=n-1 and 0<=y<=n-1 and a[x][y]==0:
#                 a[x][y] = "*"
#                 dis[x][y] = dis[tmp[0]][tmp[1]]+1
#                 dQ.append((x, y))
#                 print(f"turn:{turn}, i:{i}")
#                 for i in dis:
#                     for j in i:
#                         print(j, end=" ")
#                     print()
#                 print()
#                 # print("a")
#                 # for i in dis:
#                 #     for j in i:
#                 #         print(j, end=" ")
#                 #     print()
#                 # print()
        
#         turn += 1
#     if dis[n-1][n-1]==0:
#         print(-1)
#     else:
#         print(dis[n-1][n-1])

# if __name__=="__main__":
#     with open('in6.txt') as sys.stdin:
#         n = 7
#         a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
#         dx = [-1, 0, 1, 0]
#         dy = [0, 1, 0, -1]
#         dis = [[0]*n for _ in range(n)]
#         for i in a:
#             for j in i:
#                 print(j, end=" ")
#             print()
#         print()
#         a[0][0] = 1
#         BFS(n)
#%%
import sys
from collections import deque

def BFS(n):
    dQ = deque()
    dQ.append((0, 0))
    while dQ:
        tmp = dQ.popleft()
        for i in range(4):
            x = tmp[0]+dx[i]
            y = tmp[1]+dy[i]
            if 0<=x<=n-1 and 0<=y<=n-1 and a[x][y]==0:
                a[x][y] = a[tmp[0]][tmp[1]]+1
                dQ.append((x, y))
    if a[n-1][n-1]==0:
        print(-1)
    else:
        print(a[n-1][n-1])

if __name__=="__main__":
    # with open('in6.txt') as sys.stdin:
    n = 7
    a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    BFS(n)

# %%
