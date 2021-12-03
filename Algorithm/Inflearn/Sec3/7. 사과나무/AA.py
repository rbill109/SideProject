import sys
n = int(sys.stdin.readline())
grid = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
mid = n//2
tot = 0
row = -1
for idx, g in enumerate(grid):
    if idx <= mid:
        row += 1
        tot += sum(g[mid-row:mid+row+1])
    else:
        row -= 1
        tot += sum(g[mid-row:mid+row+1])  
print(tot)



# solution
# n=int(input())
# a=[list(map(int, input().split())) for _ in range(n)]
# res=0
# s=e=n//2
# for i in range(n):
#     for j in range(s, e+1):
#         res+=a[i][j]
#     if i<n//2:
#         s-=1
#         e+=1
#     else:
#         s+=1
#         e-=1
# print(res)



# %%
