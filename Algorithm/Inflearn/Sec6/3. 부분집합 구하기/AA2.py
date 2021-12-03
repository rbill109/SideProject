import sys

def DFS(v, n):
    if v==n+1:
        print(*list(filter(lambda x: ch[x] == 1, range(1,n+1))), sep=" ")
        return

    else:
        ch[v] = 1
        DFS(v+1, n)

        ch[v] = 0
        DFS(v+1, n)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    ch = [0]*(N+1)
    DFS(1, N)