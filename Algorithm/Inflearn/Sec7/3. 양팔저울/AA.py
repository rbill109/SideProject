#%%
import time
st = time.time()
import sys

def DFS(v, tot):
    # print(f"visit: {v}")
    global res
    if v==n:
        if 0<tot<=total:
            res.add(tot)        
    else:
        DFS(v+1, tot+a[v])
        DFS(v+1, tot-a[v])
        DFS(v+1, tot)
    
if __name__ == "__main__":
    with open('in5.txt') as sys.stdin:
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        total = sum(a)
        res = set()
        DFS(0, 0)
        print(total-len(res))
print(time.time()-st)

#%%
# solution
# import sys

# def DFS(L, sum):
#     global res
#     if L==n:
#         if 0<sum<=s:
#             res.add(sum)
#     else:
#         DFS(L+1, sum+G[L])
#         DFS(L+1, sum-G[L])
#         DFS(L+1, sum)

# if __name__=="__main__":
#     n = int(sys.stdin.readline())
#     G = list(map(int, sys.stdin.readline().split()))
#     s=sum(G)
#     res=set()
#     DFS(0, 0)
#     print(s-len(res))
  



