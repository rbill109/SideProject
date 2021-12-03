import sys
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

dic1 = dict(zip(set(a),[0]*len(a)))
dic2 = dict(zip(set(b),[0]*len(b)))

for i in a:
    for key in dic1.keys():
        if i == key:
            dic1[key] += 1

for i in b:
    for key in dic2.keys():
        if i == key:
            dic2[key] += 1

if dic1==dic2:
    print("YES")
else:
    print("NO")