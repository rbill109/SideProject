import sys
req = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
for num in range(n):
    timetable = sys.stdin.readline().strip()
    s = 0
    for i in timetable:
        if i in req:
            s += 1 
            if i != req[s-1]:               
                print(f"#{num+1} NO")
                break
    else:
        if s == len(req):
            print(f"#{num+1} YES")
        else:
            print(f"#{num+1} NO")