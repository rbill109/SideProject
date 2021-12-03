#%%
import time
st = time.time()
import sys

def DFS(v, m1, m2, m3):
    # print(f"visit: {v}, money: {m1, m2, m3}")
    global res
    if v==N:
        if m1 != m2 and m2 != m3 and m3 != m1:
            dif = max(m1, m2, m3)-min(m1, m2, m3)
            if dif < res: 
                res = dif

    else:
        DFS(v+1, m1+a[v], m2, m3)
        DFS(v+1, m1, m2+a[v], m3)
        DFS(v+1, m1, m2, m3+a[v])

if __name__ == "__main__":
    with open('in5.txt') as sys.stdin:
        N = int(sys.stdin.readline())
        a = [int(sys.stdin.readline()) for _ in range(N)]
        res = 2147000000
        DFS(0, 0, 0, 0)
        print(res)
print(time.time()-st)





#%%
# solution
import time
st = time.time()

import sys

def DFS(L):
    # print(f"visit: {L}, money: {money}")
    global res
    if L==n:
        cha = max(money)-min(money)
        if cha<res:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp)==3:
                res=cha
    else:
        for i in range(3):
            money[i]+=coin[L]
            DFS(L+1)
            money[i]-=coin[L]

if __name__=="__main__":
    with open('in5.txt') as sys.stdin:
        n=int(sys.stdin.readline())
        coin = []
        # tmp = []
        money = [0]*3
        res = 2147000000
        coin = [int(sys.stdin.readline()) for _ in range(n)]
        DFS(0)
        print(res)


        
print(time.time()-st)
# %%
