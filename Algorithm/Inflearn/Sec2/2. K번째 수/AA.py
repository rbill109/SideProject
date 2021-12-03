import sys
case = int(sys.stdin.readline())
for c in range(case):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    res = sorted(a[s-1:e])
    print(f"#{c+1} {res[k-1]}")



# solution
# T=int(input())
# for t in range(T):
#     n, s, e, k=map(int, input().split())
#     a=list(map(int, input().split()))
#     a=a[s-1:e]
#     a.sort()
#     print("#%d %d" %(t+1, a[k-1]))