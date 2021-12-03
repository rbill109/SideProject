import sys
def Count(array, target):
    start = a[0]
    cnt = 1
    for i in a:
        if i >= start + target:
            cnt += 1
            start = i
    return(cnt)


n, c = map(int, sys.stdin.readline().split())
a = [int(sys.stdin.readline()) for _ in range(n)]
a.sort()
left = 1
right = max(a)
while left <= right:
    distance = (left+right)//2
    if Count(a, distance) >= c:
        res = distance
        left = distance + 1
    else:
        right = distance - 1
print(res)




# solution
# import sys
# def Count(len):
#     cnt=1
#     ep=Line[0]
#     for i in range(1, n):
#         if Line[i]-ep>=len:
#             cnt+=1
#             ep=Line[i]
#     return cnt

# n, c = map(int, sys.stdin.readline().split())
# Line=[]
# for _ in range(n):
#     tmp=int(sys.stdin.readline())
#     Line.append(tmp)
# Line.sort()
# lt=1
# rt=Line[n-1]
# while lt<=rt:
#     mid=(lt+rt)//2
#     if Count(mid)>=c:
#         res=mid
#         lt=mid+1
#     else:
#         rt=mid-1

# print(res)

