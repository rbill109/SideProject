import sys
from collections import deque
requ = sys.stdin.readline().strip()
N = int(sys.stdin.readline())
for idx in range(N):
    prev = ""
    plan = deque(sys.stdin.readline().strip())
    req = deque(requ)
    while plan and req:
        if plan[0] == req[0]: 
            prev = req[0]
            req.popleft()
        else:
            if plan[0] != prev and plan[0] in req: # 필수 과목이나 순서가 틀린 경우
                break
        plan.popleft()
        if len(plan) < len(req): # 필수과목을 모두 수강하지 못한 경우
            break

    if len(req) == 0:
        print(f"#{idx+1} YES")
    else:
        print(f"#{idx+1} NO")