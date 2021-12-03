import sys
a = list(sys.stdin.readline().strip())
stack = []
for i in a:
    if i.isdecimal():
        stack.append(int(i))
    else:
        if i == "+":
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n1+n2)
        elif i == "-":
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2-n1)
        elif i == "*":
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n1*n2)
        elif i == "/":
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2/n1)
print(stack.pop())




