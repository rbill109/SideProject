import sys
n = int(sys.stdin.readline())
note = [sys.stdin.readline().strip() for _ in range(n)]
poem = [sys.stdin.readline().strip() for _ in range(n-1)]
word = set(note)-set(poem)
print(*word)











# solution
# import sys
# n = int(sys.stdin.readline())
# p = dict()
# for i in range(n):
#     word = sys.stdin.readline()
#     p[word] = 1
# for i in range(n-1):
#     word = sys.stdin.readline()
#     p[word] = 0
# for key, val in p.items():
#     if val==1:
#         print(key)
#         break