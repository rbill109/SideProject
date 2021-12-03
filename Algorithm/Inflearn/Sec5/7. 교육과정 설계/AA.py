# solution
import sys
from collections import deque
need = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
for i in range(n):
    plan = sys.stdin.readline().strip()
    dq=deque(need)
    for x in plan:
        if x in dq:
            if x!=dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq)==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))
