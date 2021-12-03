#%%
# Bottom-Up
import sys

n = int(sys.stdin.readline())
dy = [0]*(n+1)
dy[1] = 1
dy[2] = 2
for len in range(3, n+2):
    dy[len] = dy[len-1] + dy[len-2]
print(dy[n+1])

#%%
# Top-Down
import sys

def DFS(len):
    print(f"visit:{len}")
    if dy[len]>0:
        return dy[len]
    if len==1 or len==2:
        return len
    else:
        dy[len] = DFS(len-1) + DFS(len-2)
        return dy[len]

if __name__=="__main__":
    # n = int(sys.stdin.readline())
    n = 7
    dy = [0]*(n+2)
    print(DFS(n+1))
# %%
