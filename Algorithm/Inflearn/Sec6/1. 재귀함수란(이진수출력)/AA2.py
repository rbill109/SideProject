import sys

def DFS(n):
    if n>0:
        res = n//2
        DFS(res)
        print(n%2, end="")
    else:
        return

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    DFS(N)


