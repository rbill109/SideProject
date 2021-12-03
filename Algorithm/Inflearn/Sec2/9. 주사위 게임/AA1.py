import sys
n = int(sys.stdin.readline())
res = []
for _ in range(n):
    a = list(map(int, input().split())) 
    a.sort() 
    if a[0] == a[2]:   # rule 1
        prize = 10000 + a[0]*1000
    else:
        if a[1] == a[2] or a[0] == a[1]:   # rule 2
            prize = 1000 + a[1]*100
        else:   # rule 3
            prize = a[2]*100
    res.append(prize)
print(max(res))