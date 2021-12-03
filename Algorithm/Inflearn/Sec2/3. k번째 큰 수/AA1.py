import sys
n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
a_set = set()
num = []
for i in range(n-3):
    for j in range(i+1,n-1):
        for r in range(j+1,n):
            a_set.add(a[i]+a[j]+a[r])
res = sorted(list(a_set),reverse=True)
print(res[k-1])
