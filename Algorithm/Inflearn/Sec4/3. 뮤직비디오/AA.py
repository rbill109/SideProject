import sys
def Count(array, target):
    sum = 0
    cnt = 1
    for i in array:
        if sum+i <= target:
            sum += i
        else:
            cnt += 1
            sum = i
    return(cnt)

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
left = max(a)
right = sum(a)
while left <= right:
    length = (left+right)//2
    if Count(a, length) <= m:
        res = length
        right = length - 1
    else:
        left = length + 1
print(res)




# solution
# import sys
# def Count(capacity):
#     cnt=1
#     sum=0
#     for x in Music:
#         if sum+x>capacity:
#             cnt+=1
#             sum=x
#         else:
#             sum+=x
#     return cnt

# n, m = map(int, sys.stdin.readline().split())
# Music = list(map(int, sys.stdin.readline().split()))
# maxx=max(Music)
# lt=1
# rt=sum(Music)
# res=0
# while lt<=rt:
#     mid=(lt+rt)//2
#     if mid>=maxx and Count(mid)<=m:
#         res=mid
#         rt=mid-1
#     else:
#         lt=mid+1
# print(res)

