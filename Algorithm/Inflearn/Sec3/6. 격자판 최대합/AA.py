#!/usr/bin/env python
"""
Created on Thu Jan 14 2021

@author: yumin cho
"""
import sys
n = int(sys.stdin.readline())
grid = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
diagsum1 = diagsum2 = 0
for row in range(n):
    diagsum1 += grid[row][row]
    diagsum2 += grid[row][n-1-row]
max_row = max(map(sum,grid))
max_col = max(map(sum,(zip(*grid))))    
print(max(max_col,max_row,diagsum1,diagsum2))

    

# solution
# n=int(input())
# a=[list(map(int, input().split())) for _ in range(n)]
# largest=-2147000000
# for i in range(n):
#     sum1=sum2=0
#     for j in range(n):
#         sum1+=a[i][j]
#         sum2+=a[j][i]
#     if sum1>largest:
#         largest=sum1
#     if sum2>largest:
#         largest=sum2
# sum1=sum2=0
# for i in range(n):
#     sum1+=a[i][i]
#     sum2+=a[i][n-i-1]
# if sum1>largest:
#     largest=sum1
# if sum2>largest:
#     largest=sum2
# print(largest)


