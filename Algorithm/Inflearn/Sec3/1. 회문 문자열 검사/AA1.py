import sys
n = int(sys.stdin.readline())
for i in range(n):
    a = sys.stdin.readline().strip().upper()
    rev = a[::-1]
    if rev == a:
        print(f"#{i+1} YES")
    else:
        print(f"#{i+1} NO")