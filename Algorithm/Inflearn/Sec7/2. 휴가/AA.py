#%%
import time
st = time.time()
import sys

def DFS(v, tot):
    # print(f"visit:{v}, tot:{tot}")
    global res
    if v==n:
        if tot > res:
            res = tot
    else:
        if v+a[v][0] <= n:  
            DFS(v+a[v][0], tot+a[v][1])
        DFS(v+1, tot)
        


if __name__ == "__main__":
    with open('in2.txt') as sys.stdin:
        n = int(sys.stdin.readline())
        a = []
        for _ in range(n):
            t, p = map(int, sys.stdin.readline().split())
            a.append([t, p])
        res = -2147000000
        DFS(0, 0)
        print(res)
        print(a)
    print(time.time()-st)

#%%
import time
st = time.time()
import sys

def DFS(v, tot):
    # print(f"visit:{v}, tot:{tot}")
    global res
    if v==n+1:
        if tot > res:
            res = tot
    else:
        if v+a[v][0] <= n+1:  
            DFS(v+a[v][0], tot+a[v][1])
        DFS(v+1, tot)
        


if __name__ == "__main__":
    with open('in2.txt') as sys.stdin:
        n = int(sys.stdin.readline())
        a = [[0, 0]]
        for _ in range(n):
            t, p = map(int, sys.stdin.readline().split())
            a.append([t, p])
        res = -2147000000
        DFS(1, 0)
        print(res)
        
    print(time.time()-st)


#%%
# solution
import time
st = time.time()
import sys

def DFS(L, sum):
    global res
    if L==n+1:
        if sum>res:
            res=sum
    else:
        if L+T[L]<=n+1:
            DFS(L+T[L], sum+P[L])
        DFS(L+1, sum)

if __name__=="__main__":
    with open('in1.txt') as sys.stdin:
        n = int(sys.stdin.readline())
        T=list()
        P=list()
        for i in range(n):
            a, b = map(int, sys.stdin.readline().split())
            T.append(a)
            P.append(b)
        res=-2147000000
        T.insert(0, 0)
        P.insert(0, 0)
        DFS(1, 0)
    print(T)
    print(res)
print(time.time()-st)
# %%
