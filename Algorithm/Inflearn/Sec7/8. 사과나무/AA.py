#%%
import sys
from collections import deque

def BFS(n):
    dQ = deque()
    dQ.append((n//2, n//2))
    sum = a[n//2][n//2]
    L=0
    while True:
        if L==n//2:
            break
        size = len(dQ)
        for _ in range(size):
            tmp = dQ.popleft()
            for j in range(4): 
                x = tmp[0]+dx[j]
                y = tmp[1]+dy[j]
                if ch[x][y]==0:
                    sum += a[x][y]
                    ch[x][y] = 1
                    dQ.append((x, y))
                print()
                for i in ch:
                    for j in i:
                        print(j, end="")
                    print()
        L+=1
    print(sum)
    
if __name__=="__main__":
    with open('in6.txt') as sys.stdin:
        n = int(sys.stdin.readline())
        a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        ch = [[0]*n for _ in range(n)]
        ch[n//2][n//2] = 1
        BFS(n)




    

# %%
