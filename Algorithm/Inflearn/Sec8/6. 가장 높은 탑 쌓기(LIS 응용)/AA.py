#%%
import sys

if __name__=="__main__":
    # with open('in1.txt') as sys.stdin:
    n = int(sys.stdin.readline())
    a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    a.sort(reverse=True)
    dy = [0]*n
    dy[0] = a[0][1]
    res = 0
    for i in range(1, n):
        hgt = 0
        for j in range(i-1, -1, -1):
            if a[j][2]>a[i][2] and dy[j]>hgt:
                hgt = dy[j]
        dy[i] = hgt + a[i][1]
        if dy[i] > res:
            res = dy[i]
    print(res)

#%%
# solution
# import sys

# if __name__=="__main__":
#     n = int(input())
#     bricks = []
#     for i in range(n):
#         a, b, c=map(int, input().split())
#         bricks.append((a, b, c))
#     bricks.sort(reverse=True)
#     dy=[0]*n
#     dy[0]=bricks[0][1]
#     res=bricks[0][1]
#     for i in range(1, n):
#         max_h=0
#         for j in range(i-1, -1, -1):
#             if bricks[j][2]>bricks[i][2] and dy[j]>max_h:
#                 max_h=dy[j]
#         dy[i]=max_h+bricks[i][1]
#         res=max(res, dy[i])
#     print(res)