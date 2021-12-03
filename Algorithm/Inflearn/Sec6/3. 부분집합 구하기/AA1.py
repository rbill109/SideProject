import sys

def DFS(v):
    if v > n:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end=" ")
        print()
    else:
        # left node
        ch[v] = 1
        DFS(v+1)
        # right node
        ch[v] = 0
        DFS(v+1)     
# with open('in1.txt') as sys.stdin:
if __name__=="__main__":
    n = int(sys.stdin.readline())
    ch=[0]*(n+1)
    DFS(1)
