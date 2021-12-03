#%%
import time
st = time.time()
import sys
with open('in5.txt') as sys.stdin:
    a = list(sys.stdin.readline().strip())
    prev = "("
    s = res = 0
    for i in a[1:]:
        if i == prev and i == "(":
            s += 1
        elif i == prev and i == ")":
            s -= 1
            res += 1
        elif i != prev and i == ")":
            res += s
        prev = i
    print(res)
print(time.time()-st)







#%%
# solution
import time
st = time.time()
import sys
with open('in5.txt') as sys.stdin:
    a = list(sys.stdin.readline().strip())
    stack=[]
    cnt=0
    for i in range(len(a)):
        if a[i]=='(':
            stack.append(a[i])
        else:
            stack.pop()
            if a[i-1]=='(':
                cnt+=len(stack)
            else:
                cnt+=1
    print(cnt)
print(time.time()-st)
# %%
