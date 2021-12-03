#%%
import sys

def DFS(x, y):
    global cnt
    # print(f"visit:{v}")
    # for i in board:
    #     for j in i:
    #         print(j, end="")
    #     print()
    # print()

    if (x, y) == (n-1, n-1):
        # print("FOUND")
        cnt += 1
    else:
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<=n-1 and 0<=yy<=n-1 and board[xx][yy]==0:
                board[xx][yy] = "*"
                DFS(xx, yy)
                board[xx][yy] = 0
                

if __name__=="__main__":
    # with open('in6.txt') as sys.stdin:
    n = 7
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    board[0][0] = 1
    DFS(0, 0)
    print(cnt)


    
# %%
