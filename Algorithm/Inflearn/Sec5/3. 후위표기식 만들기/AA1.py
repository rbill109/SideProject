import sys
# with open('in2.txt') as sys.stdin:
a = list(sys.stdin.readline().strip())
stack = []
res = ""
for i in a:
    if i.isdecimal():
        res += i
    else:
        if i == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop()
        else:
            if i in ["+","-"]:
                while stack and stack[-1] != "(":
                    res += stack.pop()    
            elif i in ["*","/"]:
                while stack and stack[-1] == "(":
                    if stack[-1] in ["*","/"]:
                        res += stack.pop()    
            stack.append(i)

if len(stack)!=0:
    while stack:
        res += stack.pop()
print(res)