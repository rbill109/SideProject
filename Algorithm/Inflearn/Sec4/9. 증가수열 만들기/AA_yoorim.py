import sys
n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))
res = 0; cnt = 0
result = []


while len(l)>0:
    a = (l[0],'L')
    b = (l[-1],'R')
    if min(a,b)[0] > res:
        result.append(min(a,b)[1])
        cnt += 1
        if min(a,b)[1]=='R':
            res = l.pop()
        else:
            res = l.pop(0)
    elif max(a,b)[0] > res:
        result.append(max(a,b)[1])
        cnt += 1
        if max(a,b)[1]=='R':
            res = l.pop()
        else:
            res = l.pop(0)
    else:
        break

print(cnt)
print("".join(result))