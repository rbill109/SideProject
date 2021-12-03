import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
que = deque(range(1,N+1))
idx = 0
while len(que) > 1:
    idx += 1
    cand = que.popleft()
    if idx == K:
        idx = 0
    else:
        que.append(cand)
print(que[0])

# import sys
# from collections import deque
# N, K = map(int, sys.stdin.readline().split())
# que = deque(range(1,N+1))
# idx = 0
# while len(que) > 1:
#     idx += 1
#     if idx == K:
#         idx = 0
#         que.popleft()
#     else:
#         que.rotate(-1)
# print(que[0])