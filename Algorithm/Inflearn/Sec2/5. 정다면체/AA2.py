import sys
N, M = map(int, sys.stdin.readline().split())

table = [0]*(N+M+1)
for i in range(1, N+1):
    for j in range(1, M+1):
        table[i+j] += 1
print(*[idx for idx, i in enumerate(table) if i == max(table)], sep=" ")

# import sys
# from collections import defaultdict

# N, M = map(int, sys.stdin.readline().split())
# table = defaultdict(int)
# for i in range(1, N+1):
#     for j in range(1, M+1):
#         table[i+j] += 1
# print(*[k for k, v in table.items() if v == max(table.values())], sep=" ")