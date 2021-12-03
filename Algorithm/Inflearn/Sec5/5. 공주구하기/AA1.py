import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
deq = deque(range(1,n+1))
while len(deq)>1:
    for _ in range(k-1):
        deq.rotate(-1)        
    deq.popleft()
print(deq[0])

