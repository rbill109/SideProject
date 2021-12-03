# #%%
# # import time
# # st = time.time()
# import sys

# def DFS(v, idx):
#     global cnt
#     # print(f"visit:{v}, index:{idx}")
#     if v==n:
#         cnt +=1
#         for j in range(idx):
#             print(chr(alp[j]+64), end='')
#         print()

#     else:
#         for i in range(1, 27):
#             if i<10: 
#                 if a[v]==i:
#                     alp[idx] = i
#                     DFS(v+1, idx+1)
#             else:
#                 if int(''.join(map(str, a[v:v+2])))==i:
#                     alp[idx] = i
#                     DFS(v+2, idx+1)


# if __name__=="__main__":
#     # with open('in5.txt') as sys.stdin:
#     a = list(map(int, sys.stdin.realine()))
#     n = len(a)
#     cnt = 0
#     alp = [0]*n
#     DFS(0, 0)
#     print(cnt)
# print(time.time()-st)



#%%
# import time
# st = time.time()
import sys

def DFS(v,P):
    global cnt
    if v==n:
        cnt+=1
        for j in range(P):
            print(chr(res[j]+64), end='')
        print()
    else:
        for i in range(1, 27):
            if i <10:
                if code[v]==i:
                    res[P]=i	
                    DFS(v+1, P+1)
            else:
                if code[v]==i//10 and code[v+1]==i%10:
                    res[P]=i
                    DFS(v+2, P+1)

if __name__=="__main__":
    with open('in5.txt') as sys.stdin:
        code = list(map(int, sys.stdin.readline().strip()))
        print(code)
        n=len(code)
        code.insert(n, -1)
        res=[0]*n
        cnt=0
        DFS(0, 0)
        print(cnt)
# print(time.time()-st)
# %%
