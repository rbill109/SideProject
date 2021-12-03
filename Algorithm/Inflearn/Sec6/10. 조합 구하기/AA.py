#%%
import sys

def DFS(v, s):
    print(f"\nvisit:{v} start:{s}")
    global cnt
    if v==m:
        for i in a:
            print(i, end=' ')
        print()
        cnt+=1

    else:
        for i in range(s, n+1): 
            a[v]=i
            DFS(v+1, i+1)

        # for i in range(s, n+1):
        #     if check[i] == 0:
        #         check[i] = 1
        #         a[v] = i
        #         DFS(v+1, 1)
        #         check[i] = 0


if __name__=="__main__":
    with open('in2.txt') as sys.stdin:
        n, m = map(int, sys.stdin.readline().split())
        a = [0]*m
        cnt=0
        check = [0]*(n+1)
        DFS(0, 1)
        print(cnt)

# %%
# solution
# import sys

# def DFS(v, s):
#     global cnt
#     if v==m:
#         for i in range(m):
#             print(a[i], end=' ')
#         print()
#         cnt+=1
#     else:
#         for i in range(s, n+1):
#             a[v]=i
#             DFS(v+1, i+1)
           
# if __name__=="__main__":
#     n, m = map(int, sys.stdin.readline().split())
#     a = [0]*(n+1)
#     cnt=0
#     DFS(0, 1)
#     print(cnt)

# %%
a = list(range(6))
print(a)
for i in range(3, 3):
    a[0] = i
print(a)

# %%
