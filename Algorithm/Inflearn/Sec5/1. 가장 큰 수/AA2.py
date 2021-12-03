import sys
a, m = map(int, sys.stdin.readline().split())
a = list(map(int, str(a)))
stack = []
for i in a:
    # print(i, stack[-1])
    # print(i, stack)
    while stack and m>0:
        if stack[-1] < i:
            stack.pop()
            # print(f"head on {i} after pop: stack={stack}")
            m -= 1
        else:
            break
    stack.append(i)
if m>0:
    stack = stack[:-m]
print(*stack, sep="")
