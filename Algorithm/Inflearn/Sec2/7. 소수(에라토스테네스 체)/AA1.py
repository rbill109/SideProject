import sys
n = int(sys.stdin.readline())
prime = 0
for i in range(2, n+1):
    cnt = 0
    for j in range(2, i):
        if i % j != 0:
            cnt += 1
        else:
            cnt = 0
            break
    if cnt > 0:
        prime += 1
print(prime+1)