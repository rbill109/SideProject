#%%
import time
st = time.time()
import sys

def DFS(v, tot_score, tot_time):
    print(f"visit: {v}")
    global res
    # if tot_time > m:
    #     return
    if v==n:
        if tot_score > res:
            res = tot_score
    else:
        DFS(v+1, tot_score+a[v][0], tot_time+a[v][1])
        DFS(v+1, tot_score, tot_time)

if __name__ == "__main__":
    with open('in1.txt') as sys.stdin:
        n, m = map(int, sys.stdin.readline().split())
        a = []
        for _ in range(n):
            tot_score, tot_time = map(int, sys.stdin.readline().split())
            a.append([tot_score, tot_time])
        res = -2147000000
        DFS(0, 0, 0)
        print(res)

print(time.time()-st)

#%%
import time
st = time.time()
import sys

def DFS(v, tot_score, tot_time):
    global res
    if tot_time > m:
        return
    if v==n:
        if tot_score > res:
            res = tot_score
    else:
        for i in range(v, n):
            DFS(i+1, tot_score+a[i][0], tot_time+a[i][1])


if __name__ == "__main__":
    with open('in5.txt') as sys.stdin:
        n, m = map(int, sys.stdin.readline().split())
        a = []
        for _ in range(n):
            tot_score, tot_time = map(int, sys.stdin.readline().split())
            a.append([tot_score, tot_time])
        res = -2147000000
        DFS(0, 0, 0)
        print(res)

print(time.time()-st)


#%%
# solution
import time
st = time.time()
import sys

def DFS(L, sum, time):
    global res
    if time>m:
        return
    if L==n:
        if sum>res:
            res=sum
    else:
        DFS(L+1, sum+pv[L], time+pt[L])
        DFS(L+1, sum, time)

if __name__=="__main__":
    with open('in5.txt') as sys.stdin:
        n, m = map(int, sys.stdin.readline().split())
        pv=list()
        pt=list()
        for i in range(n):
            a, b = map(int, sys.stdin.readline().split())
            pv.append(a)
            pt.append(b)
        res=-2147000000
        DFS(0, 0, 0)
        print(res)

    print(time.time()-st)

# %%
