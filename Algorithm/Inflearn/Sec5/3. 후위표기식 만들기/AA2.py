import sys
a = sys.stdin.readline().strip()

# (3+5)*2  ->  35+2*
# 3*(5+2)-9  ->  352+*9-
# 5+7*3-5+(3+2*3) -> 573*+5-323*++
stack = []
res = ""
for i in a:
    if i.isdecimal():
        res += i
    else:
        if i=="(":
            stack.append(i)
        elif i in ("+","-"): 
            if stack and stack[-1] in ("*","/"):
                while stack and stack[-1] !="(":
                    res += stack.pop()
            elif stack and stack[-1] in ("+","-"):
                while stack and stack[-1] !="(":
                    res += stack.pop()
            
            stack.append(i)
        elif i in ("*","/"):
            stack.append(i)
        elif i==")":                
            while stack and stack[-1] !="(":
                res += stack.pop()
            stack.pop()
            if stack and stack[-1] in ("*","/"):
                res += stack.pop()
    # print(f"i:{i},stack:{stack}, res:{res}") 

while stack and stack[-1] != "(":
    res += stack.pop()
    # print(f"i:{i},stack:{stack}, res:{res}")      

print(res)

