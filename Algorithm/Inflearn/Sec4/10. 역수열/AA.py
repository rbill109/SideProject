import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))[::-1]
seq = []
for i in a:
    seq.insert(i, n)
    n -= 1
print(*seq, sep=" ")


# import sys
# n = int(sys.stdin.readline())
# a = list(map(int, sys.stdin.readline().split()))
# seq = [0]*n
# for rev_idx, rev in enumerate(a):
#     i = -1
#     zero = 0
#     while zero <= rev:
#         i += 1
#         if seq[i]==0:
#             zero += 1
#     seq[i] = rev_idx+1
# print(*seq, sep=" ")




# solution
# import sys
# n = int(sys.stdin.readline())
# a = list(map(int, sys.stdin.readline().split()))
# seq=[0]*n
# for i in range(n):
#     for j in range(n):
#         if(a[i]==0 and seq[j]==0):
#             seq[j]=i+1
#             break
#         elif seq[j]==0:
#             a[i]-=1
# for x in seq:
#     print(x, end=' ')


# %%
