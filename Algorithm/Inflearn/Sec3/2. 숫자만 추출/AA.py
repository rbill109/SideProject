import sys
n = sys.stdin.readline()
num = ""
for i in n:
    if i.isdecimal():
        num += i
num = int(num)
cnt = 0
for i in range(1,num+1):
    if num % i == 0:
        cnt += 1
print(num)
print(cnt)





# solution
# import sys
# s=input()
# res=0
# for x in s:
#     if x.isdecimal():
#         res=res*10+int(x)
# print(res)
# cnt=0
# for i in range(1, res+1):
#     if res%i==0:
#         cnt+=1
# print(cnt)
