#%%
# DFS
import sys

def DFS(x, y):
    global cnt
    board[x][y] = "*"
    cnt += 1
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<n and 0<=yy<n and board[xx][yy]==1:
            DFS(xx, yy)

if __name__=="__main__":
    n = int(sys.stdin.readline())
    board = [list(map(int, sys.stdin.readline())) for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    res=[]
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                cnt=0
                DFS(i, j)
                res.append(cnt)
    print(len(res))
    res.sort()
    for x in res:
        print(x)

#%%
import sys

def DFS(x, y):
    for i in board:
        print(*i, sep="")
    print()
    global cnt
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<n and 0<=yy<n and board[xx][yy]==1:
            board[xx][yy] = "*"
            cnt += 1
            DFS(xx, yy)
        

if __name__=="__main__":
    with open('in6.txt') as sys.stdin:
        n = int(sys.stdin.readline())
        board = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
        for i in board:
            print(*i, sep="")
        print()
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        cnt = 0
        res=[]
        DFS(0, 0)   
        # for i in range(n):
        #     for j in range(n):
        #         if board[i][j]==1:
        #             cnt=0
        #             DFS(i, j)
        #             res.append(cnt)
        res.append(cnt)
        print(len(res))
        res.sort()
        for x in res:
            print(x)
# %%
import sys
from collections import deque

def DFS(x, y):
    for i in board:
        print(*i, sep="")
    print()
    global cnt
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<n and 0<=yy<n and board[xx][yy]==1:
            board[xx][yy] = "*"
            cnt += 1
            DFS(xx, yy)
        

if __name__=="__main__":
    with open('in6.txt') as sys.stdin:
        n = int(sys.stdin.readline())
        board = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
        for i in board:
            print(*i, sep="")
        print()
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        cnt = 0
        res=[]
        DFS(0, 0)   
        # for i in range(n):
        #     for j in range(n):
        #         if board[i][j]==1:
        #             cnt=0
        #             DFS(i, j)
        #             res.append(cnt)
        res.append(cnt)
        print(len(res))
        res.sort()
        for x in res:
            print(x)