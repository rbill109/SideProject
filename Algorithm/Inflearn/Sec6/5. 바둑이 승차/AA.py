#%%
# import sys

# def DFS(v, tot):
#     global largest
#     if tot > c:
#         return
#     elif v==n:
#         if tot > largest:
#             largest = tot
#     else:
#         # left node
#         DFS(v+1, tot+a[v])
#         # right node
#         DFS(v+1, tot)

# if __name__=="__main__":
# # with open('in1.txt') as sys.stdin:
#     c, n = map(int, sys.stdin.readline().split())
#     a = [int(sys.stdin.readline()) for _ in range(n)]
#     tot = sum(a)
#     largest = 0
#     if tot > c:
#         DFS(0, 0)
#         print(largest)
#     else:
#         print(tot)


#%%
# solution
# import sys

# def DFS(L, sum, tsum):
#     global result
#     print(L, sum, result)
#     if sum+(total-tsum)<result:
#         return
#     if sum>c:
#         return
#     if L==n:
#         if sum>result:
#             result=sum
#     else:
#         DFS(L+1, sum+a[L], tsum+a[L])
#         DFS(L+1, sum, tsum+a[L])
#     # print(L, result)


# if __name__=="__main__":
#     # with open('in5.txt') as sys.stdin:
#     c, n = map(int, sys.stdin.readline().split())
#     a = [int(sys.stdin.readline()) for _ in range(n)]
#     result=-2147000000
#     total=sum(a)
#     DFS(0, 0, 0)
#     print(result)



# %%
