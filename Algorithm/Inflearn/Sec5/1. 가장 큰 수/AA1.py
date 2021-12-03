import sys    
a, m = map(int, sys.stdin.readline().split())
a = list(map(int, str(a)))
res = []
for i in a: 
    while res and m>0 and res[-1] < i:
        res.pop()
        m -= 1
    res.append(i)
if m>0:
    res = res[:-m]
print(*res, sep="")








