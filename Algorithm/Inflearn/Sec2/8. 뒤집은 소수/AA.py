def reverse(x):
    # rev = []
    # for i in reversed([i for i in str(x)]):
    #     rev.append(i)
    #     res = int("".join(rev))
    return(int(str(x)[::-1]))    # faster than res
def isPrime(x):
    if x == 1:
        return False
    else:
        for i in range(2, x//2+1):    # faster than range(2, x)
            if x % i == 0:
                return False
        else:
            return True

import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

for x in a:
    rev = reverse(x)
    if isPrime(rev):
        print(rev, end=' ')

# solution
# n=int(input())
# a=list(map(int, input().split()))
# def reverse(x):
#     res=0
#     while x>0:
#         t=x%10
#         res=res*10+t
#         x=x//10
#     return res

# def isPrime(x):
#     if x==1:
#         return False
#     for i in range(2, x):
#         if x%i==0:
#             return False
#     return True

# for x in a:
#     tmp=reverse(x)
#     if isPrime(tmp):
#         print(tmp, end=' ')
