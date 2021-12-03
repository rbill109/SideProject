import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
s = sq = 0
e = n-1
dir = ""
while s <= n:
    if a[s] > sq and a[e] > sq:
        if a[s] < a[e]:
            sq = a[s]
            dir += "L"
            s += 1
        else:
            sq = a[e]
            dir += "R"
            e -= 1 
    elif a[s] > sq:
        sq = a[s]
        dir += "L"
        s += 1
    elif a[e] > sq:
        sq = a[e]
        dir += "R"
        e -= 1
    else:
        break
print(len(dir))
print(dir)    