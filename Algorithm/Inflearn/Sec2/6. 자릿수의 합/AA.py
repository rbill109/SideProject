def digit_sum(x):
    digit = 0
    for i in str(x):
        digit += int(i)
    return digit

import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

sum_ls = [digit_sum(i) for i in a]
print(a[sum_ls.index(max(sum_ls))])


# solution
# def digit_sum(x):
#     sum=0
#     while x>0:
#         sum+=x%10
#         x=x//10
#     return sum

# n=int(input())
# a=list(map(int, input().split()))
# res=0
# max=-2147000000
# for x in a:
#     tot=digit_sum(x)
#     if tot>max:
#         max=tot
#         res=x
# print(res)
