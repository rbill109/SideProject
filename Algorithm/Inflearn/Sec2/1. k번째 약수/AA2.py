import sys
N, K = map(int, sys.stdin.readline().split())

ord = 0
for i in range(1,N+1):
    if N%i==0:
        ord += 1
        if ord == K:
            print(i)
            break
if ord < K:
    print(-1)
