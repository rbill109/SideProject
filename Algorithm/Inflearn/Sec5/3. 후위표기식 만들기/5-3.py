import sys
# sys.stdin = open("input.txt","rt")
num = list(map(str,input()))

func = []
res = []

for x in num:
    if x not in ['+','*','/','-','(',')']:
        res.append(x)
    elif x in ['*','/']:
        while func and func[-1] in ['*','/',')']:
            if func[-1] in [')'] :
                func.pop()
                res.append(func.pop())
                func.pop()
            else:
                res.append(func.pop())
        func.append(x)
    elif x in ['+','-']:
        while func and func[-1] in ['*','/',')','+','-']:
            if func[-1] in [')'] :
                func.pop()
                res.append(func.pop())
                func.pop()
            else:
                res.append(func.pop())
        func.append(x)
    elif x == '(' or ')':
        func.append(x)

while len(func)>0:
    if func[-1] not in ['(',')']:
        res.append(func.pop())
    else:
        func.pop()

print(''.join(map(str,res)))