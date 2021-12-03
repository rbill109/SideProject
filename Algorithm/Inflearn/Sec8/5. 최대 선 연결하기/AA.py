import sys 

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    dy = [1]*n
    res = 0
    for i in range(1, n):
        len = 0
        for j in range(i-1, 0, -1):
            if a[j]<a[i]:
                if dy[j]>len:
                    len = dy[j]
        dy[i] = len+1
        if dy[i] > res:
            res = dy[i]
    print(res)