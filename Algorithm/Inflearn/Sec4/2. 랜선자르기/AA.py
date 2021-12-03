import sys
k, n = map(int, sys.stdin.readline().split())
a = [int(sys.stdin.readline().strip()) for _ in range(k)]
left = 1
right = max(a)
while left <= right:
    length = (left+right)//2
    cnt = sum(map(lambda x: x//length, a))
    if cnt >= n:
        left = length + 1
        res = length
    else:
        right = length - 1
print(res)        



# solution
# import sys   
# def Count(len):
#     cnt=0
#     for x in Line:
#         cnt+=(x//len)
#     return cnt
# k, n=map(int, sys.stdin.readline().split())
# Line=[]
# res=0
# largest=0
# for i in range(k):
#     tmp=int(sys.stdin.readline())
#     Line.append(tmp)
#     largest=max(largest, tmp)
# lt=1
# rt=largest
# while lt<=rt:
#     mid=(lt+rt)//2
#     if Count(mid)>=n:
#         res=mid
#         lt=mid+1
#     else:
#         rt=mid-1
# print(res)
