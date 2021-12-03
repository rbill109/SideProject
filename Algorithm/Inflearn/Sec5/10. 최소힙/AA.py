import sys
import heapq as hq
heap = []
# with open('in1.txt') as sys.stdin:
while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    elif n == 0:
        if len(heap) == 0:
            print(-1)
        else:
            print(hq.heappop(heap))
    else:
        hq.heappush(heap, n)










# solution
# import sys
# import heapq as hq
# a=[]
# while True:
#     n = int(sys.stdin.readline())
#     if n==-1:
#         break
#     if n==0:
#         if len(a)==0:
#             print(-1)
#         else:
#             print(hq.heappop(a))
#     else:
#         hq.heappush(a, n)