#%%
import time
st = time.time()
import sys
from collections import deque
with open('in5.txt') as sys.stdin:
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    deq = deque([(idx, val) for idx, val in enumerate(a)])
    cnt = 0
    while deq:
        patient = deq.popleft()
        # if patient[1] < max(deq,key=lambda x: x[1])[1]:
        if any(patient[1]<x[1] for x in deq):
            deq.append(patient)
        else:
            cnt+=1
            if patient[0] == m:
                print(cnt)
                break
print(time.time()-st)



# solution
# import sys
# from collections import deque
# n, m = map(int, sys.stdin.readline().split())
# Q=[(pos, val) for pos, val in enumerate(list(map(int, sys.stdin.readline().split())))]
# Q=deque(Q)
# cnt=0
# while True:
#     cur=Q.popleft()
#     if any(cur[1]<x[1] for x in Q):
#         Q.append(cur)
#     else:
#         cnt+=1
#         if cur[0]==m:
#             print(cnt)
#             break

