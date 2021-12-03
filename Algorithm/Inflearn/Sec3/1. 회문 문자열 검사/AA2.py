import sys
N = int(sys.stdin.readline())
for i in range(N):
    word = sys.stdin.readline().strip().lower()
    if word == word[::-1]:
        print(f"#{i+1} YES")
    else:
        print(f"#{i+1} NO")

