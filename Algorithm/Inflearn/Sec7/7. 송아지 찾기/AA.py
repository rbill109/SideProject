# %%
import sys
from collections import deque

def BFS(n, m):
    dQ = deque()
    dQ.append(n)
    stop = False
    while dQ:
        # print(dis)
        # print(dQ)
        now = dQ.popleft()
        # if now==m:
        #     break
        for next in (now-1, now+1, now+5):
            if 0 <= next <= MAX:
                if dis[next]==0:
                    dQ.append(next)
                    # ch[next] = 1
                    dis[next] = dis[now]+1    
                    if next == m:
                        stop = True
                        break
        if stop:
            break

    print(dis[m])

if __name__=="__main__":
    # with open('in6.txt') as sys.stdin:
    n, m = map(int, sys.stdin.readline().split())
    MAX = 10000
    dis = [0] * (MAX+1)
    BFS(n, m)

    
# %%
# solution
# import sys
# from collections import deque

# def BFS(n, m):
#     dQ = deque()
#     dQ.append(n)
#     while dQ:
#         print(dis)
#         print(dQ)
#         now = dQ.popleft()
#         if now==m:
#             break
#         for next in (now-1, now+1, now+5):
#             if 0 <= next <= MAX:
#                 if ch[next]==0:
#                     dQ.append(next)
#                     ch[next] = 1
#                     dis[next] = dis[now]+1    
#     print(dis[m])

# if __name__=="__main__":
#     with open('in6.txt') as sys.stdin:
#         n, m = map(int, sys.stdin.readline().split())
#         MAX = 30
#         ch = [0] * (MAX+1)
#         dis = [0] * (MAX+1)
#         ch[n] = 1
#         dis[n] = 0
#         BFS(n, m)
