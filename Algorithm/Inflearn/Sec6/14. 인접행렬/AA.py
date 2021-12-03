#%%
import sys

with open('in1.txt') as sys.stdin:
    n, m = map(int, sys.stdin.readline().split())
    g = [[0]*(n) for _ in range(n)]
    for i in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        g[a-1][b-1] = c

    for i in range(n):
        for j in range(n):
            print(g[i][j], end=' ')
        print()
# %%
import sys

with open('in2.txt') as sys.stdin:
    n, m = map(int, sys.stdin.readline().split())
    g = [[0]*(n) for _ in range(n)]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        g[a-1][b-1] = 1

    for i in range(n):
        for j in range(n):
            print(g[i][j], end=' ')
        print()

# %%
