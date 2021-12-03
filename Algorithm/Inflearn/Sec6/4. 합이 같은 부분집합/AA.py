#%%
import sys

def DFS(v, tot):
    # print(f"visit:{v}, tot:{tot}")
    if v==n:
        if tot==total/2:
            print("YES")
            sys.exit(0)
    else:
        # left node
        DFS(v+1, tot+a[v])
        # right node
        DFS(v+1, tot)
   

if __name__=="__main__":
    # with open('in1.txt') as sys.stdin:
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    total = sum(a)
    if total%2==0:
        DFS(0, 0)
    print("NO")
    
#%%

# solution
# import sys

# def DFS(L, sum):
#     if sum>total//2:
#         return
#     if L==n:
#         if sum==(total-sum):
#             print("YES")
#             sys.exit(0)
#     else:
#         DFS(L+1, sum+a[L])
#         DFS(L+1, sum)

# if __name__=="__main__":
#     n = int(sys.stdin.readline())
#     a = list(sys.stdin.readline().split())
#     total=sum(a)
#     DFS(0, 0)
#     print("NO")