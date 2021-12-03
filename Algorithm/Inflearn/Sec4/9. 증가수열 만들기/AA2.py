import sys
N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
lt = cnt = prev = 0
rt = N-1
text = ""
while lt < rt:
    if a[lt] < a[rt]:
        if a[lt] > prev:
            text += "L"
            prev = a[lt]
            lt += 1
        elif a[rt] > prev:
            text += "R"
            prev = a[rt]
            rt -= 1  
        else:
            break
    elif a[lt] > a[rt]:
        if a[rt] > prev:
            text += "R"
            prev = a[rt]
            rt -= 1 
        elif a[lt] > prev:
            text += "L"
            prev = a[lt]
            lt += 1
        else:
            break
    cnt += 1
print(cnt)
print(text)