# solution
import sys
n = int(sys.stdin.readline())
meeting=[]
for i in range(n):
    a, b = map(int,sys.stdin.readline().split())
    meeting.append((a, b))
meeting.sort(key=lambda x : (x[1], x[0]))
et=0
cnt=0
for x, y in meeting:
    if x>=et:
        et=y
        cnt+=1
print(cnt)