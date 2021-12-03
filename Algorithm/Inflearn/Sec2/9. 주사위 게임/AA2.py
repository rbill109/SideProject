import sys
N = int(sys.stdin.readline())
maxm = 0
for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    prize = 0
    if (a==b)&(b==c):
        prize = 10000 + a*1000
    elif (a==b)|(b==c)|(c==a):
        prize = 1000 + a*100
    else:
        prize = max(a,b,c)*100
    if maxm < prize:
        maxm = prize
print(maxm)
