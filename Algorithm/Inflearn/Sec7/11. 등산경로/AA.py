# %%
import time
st = time.time()
import sys

def DFS(x, y):
    global cnt
    if (x, y) == (max_x, max_y):
        cnt+=1
    else:
        for k in range(4):
            xx = x+dx[k]
            yy = y+dy[k]
            if 0<=xx<=n-1 and 0<=yy<=n-1 and board[xx][yy]>board[x][y]:
                DFS(xx, yy)

if __name__=="__main__":
    with open('in5.txt') as sys.stdin:
        n = int(sys.stdin.readline())
        board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]    
        maximum = max(list(map(max,board)))
        minimum = min(list(map(min,board)))
        for idx, v in enumerate(board):
            if maximum in v:
                max_x, max_y = idx, v.index(maximum)
            elif minimum in v:
                min_x, min_y = idx, v.index(minimum)
        dx=[-1, 0, 1, 0]
        dy=[0, 1, 0, -1]
        # for i in board:
        #     for j in i:
        #         print(j, end=" ")
        #     print()
        cnt = 0
        DFS(min_x, min_y)
        print(cnt)
print(time.time()-st)
# %%
# solution
import time
st = time.time()
import sys

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def DFS(x, y):
    global cnt
    if x==ex and y==ey:
        cnt+=1
    else:
        for k in range(4):
            xx=x+dx[k]
            yy=y+dy[k]
            if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>board[x][y]:
                ch[xx][yy]=1
                DFS(xx, yy)
                ch[xx][yy]=0

if __name__=="__main__":
    with open('in5.txt') as sys.stdin:
        n=int(sys.stdin.readline())
        board=[[0]*n for _ in range(n)]
        ch=[[0]*n for _ in range(n)]
        max=-2147000000
        min=2147000000
        for i in range(n):
            tmp=list(map(int, sys.stdin.readline().split()))
            for j in range(n):
                if tmp[j]<min:
                    min=tmp[j]
                    sx=i
                    sy=j
                if tmp[j]>max:
                    max=tmp[j]
                    ex=i
                    ey=j      
                board[i][j]=tmp[j]
        ch[sx][sy]=1
        cnt=0
        DFS(sx, sy)
        print(cnt)
print(time.time()-st)
# %%
