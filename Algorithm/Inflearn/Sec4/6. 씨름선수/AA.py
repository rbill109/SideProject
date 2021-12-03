#%%
import sys
n = int(sys.stdin.readline())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
a.sort(reverse=True)
wgt = cnt = 0
for p in a:
    if p[1] > wgt:
        wgt = p[1]
        cnt += 1
print(cnt)






# cnt = 0
# for i in range(n):
#     wgt = a[i][1]
#     # print(f"{i+1}번째 지원자의 몸무게:{wgt}")
#     for j in range(i+1,n):
#         if a[j][1] > wgt:
#             # print("탈락!")
#             break
#     else:
#         # print("합격!")
#         cnt += 1
# print(cnt)




# solution
# import sys
# n = int(sys.stdin.readline())
# body=[]
# for i in range(n):
#     a, b = map(int,sys.stdin.readline().split())
#     body.append((a, b))
# body.sort(reverse=True)
# largest=0
# cnt=0
# for x, y in body:
#     if y>largest:
#         largest=y
#         cnt+=1
# print(cnt)

# %%
