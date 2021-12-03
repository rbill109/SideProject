n = int(input())
a = list(map(int, input().split()))
score = [0]*n
if a[0] == 1:
    score[0] = 1
cnt = 0
for i in range(1, n):
    if a[i] == 1:
        score[i] = 1
        if a[i-1] == 1:
            cnt += 1
        else:
            cnt = 0   
        score[i] += cnt
    else:
        score[i] = 0
print(sum(score))



# solution
# n=int(input())
# a=list(map(int, input().split()))
# cnt=0
# sum=0
# for i in a:
#     if i==1:
#         cnt=cnt+1
#         sum=sum+cnt
#     else:
#         cnt=0
# print(sum)

