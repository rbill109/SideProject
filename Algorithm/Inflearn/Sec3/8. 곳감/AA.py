import sys
n = int(sys.stdin.readline())
grid = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
c = int(sys.stdin.readline())

for i in range(c):
    row, direction, num = map(int, sys.stdin.readline().split())
    num = num % n
    row -= 1
    if direction == 0:
        grid[row] = grid[row][num:]+grid[row][:num]
    else:
        grid[row] = grid[row][(n-num):]+grid[row][:(n-num)]

mid = n//2
row = mid + 1
tot = 0
for idx, g in enumerate(grid):
    if idx <= mid:
        row -= 1
        tot += sum(g[mid-row:mid+row+1])
    else:
        row += 1
        tot += sum(g[mid-row:mid+row+1])  
print(tot)


# solution
# n=int(input())
# a=[list(map(int, input().split())) for _ in range(n)]
# m=int(input())
# for i in range(m):
#     h, t, k=map(int, input().split())
#     if(t==0):
#         for _ in range(k):
#             a[h-1].append(a[h-1].pop(0))
#     else:
#         for _ in range(k):
#             a[h-1].insert(0, a[h-1].pop())
# res=0
# s=0
# e=n-1
# for i in range(n):
#     for j in range(s, e+1):
#         res+=a[i][j]
#     if i<n//2:
#         s+=1
#         e-=1
#     else:
#         s-=1
#         e+=1
# print(res)