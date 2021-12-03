import sys
a = [list(map(int,sys.stdin.readline().split())) for _ in range(7)]
cnt = 0
for i in range(7):
    for j in range(3):
        row = a[i][j:j+5]
        if row == row[::-1]:
            cnt += 1
        col = []
        for k in range(5):
            col.append(a[j+k][i])
        if col == col[::-1]:
            cnt += 1

print(cnt)




# solution
# board=[list(map(int, input().split())) for _ in range(7)]
# cnt=0
# len=5
# for i in range(3):
#     for j in range(7):
#         tmp=board[j][i:i+len]
#         if tmp==tmp[::-1]:
#             cnt+=1
#         for k in range(len//2):
#             if board[i+k][j]!=board[i+len-k-1][j]:
#                 break
#         else:
#             cnt+=1
        
# print(cnt)

