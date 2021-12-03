import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
mean = int(sum(a)/len(a)+0.5)
min_dev = 2147000000
num = 0
for idx, i in enumerate(a):
    dev = abs(i-mean)
    if dev < min_dev:
        min_dev = dev
        num = idx+1
    elif dev == min_dev:
        if i > a[num-1]:
            min_dev = dev
            num = idx+1
print(mean, num)

## first try
# import sys
# n = int(input())
# a = list(map(int, sys.stdin.readline().split()))
# mean = int(round(sum(a)/len(a),0))
# diff = {v+1:abs(a[v]-mean) for v in range(len(a))}
# mini = {k:a[k-1] for k,v in diff.items() if v == min(diff.values())}
# num = max(mini,key=mini.get)
# print(mean, num)


## solution
# n=int(input())
# a=list(map(int, input().split()))
# ave=sum(a)/n
# ave=ave+0.5
# ave=int(ave)
# min=2147000000
# for idx, x in enumerate(a):
#     tmp=abs(x-ave)
#     if tmp<min:
#         min=tmp
#         score=x
#         res=idx+1
#     elif tmp==min:
#         if x>score:
#             score=x
#             res=idx+1
# print(ave, res)
