# #%%
# import sys

# def DFS():

# if __name__=="__main__":
#     n = 10
#     board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
#     dx = [0, 1, 0]
#     dy = [1, 0, -1]
#     DFS()
#%%
# solution
import sys

def DFS(x, y):
    ch[x][y] = 1
    if x==0:
        print(y)
    else:
        if y-1>=0 and board[x][y-1]==1 and ch[x][y-1]==0:
            DFS(x, y-1)
        elif y+1<n and board[x][y+1]==1 and ch[x][y+1]==0:
            DFS(x, y+1)
        else:
            DFS(x-1, y)

if __name__=="__main__":
    n = 10
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    ch = [[0]*n for _ in range(n)]
    for y in range(n):
        if board[n-1][y]==2:
            DFS(n-1, y)