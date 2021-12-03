import sys
n = int(sys.stdin.readline())
grid = []
for _ in range(n):
    str = "0 " + sys.stdin.readline() + " 0"
    grid.append(list(map(int,str.split())))
grid.insert(0,[0]*(n+2))
grid.append([0]*(n+2))

peak = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        tot = max(
            grid[i][j-1],
            grid[i][j+1],
            grid[i-1][j],
            grid[i+1][j])
        if grid[i][j] > tot:
            peak += 1
print(peak)








# solution
# import sys
# dx=[-1, 0, 1, 0]
# dy=[0, 1, 0, -1]
# n=int(sys.stdin.readline())
# a=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# a.insert(0, [0]*n)
# a.append([0]*n)
# for x in a:
#     x.insert(0, 0)
#     x.append(0)

# cnt=0
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
#             cnt+=1
# print(cnt)
