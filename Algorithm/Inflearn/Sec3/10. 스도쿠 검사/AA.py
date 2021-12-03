import sys
def sudoku_check(a):
    line = list(range(1,10))
    row = sum(map(lambda x: 1 if sorted(x) == line else 0, a)) 
    col = sum(map(lambda x: 1 if sorted(x) == line else 0,zip(*a)))
    if row != 9 or col != 9:
        return "NO"

    for i in range(9):
        for j in range(9):
            if i%3==0 and j%3==0:
                box = a[i][j:j+3]+a[i+1][j:j+3]+a[i+2][j:j+3]
                if sorted(box) != line:
                    return "NO"
    return "YES"
    
a = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
print(sudoku_check(a))


# solution
# def check(a):
#     for i in range(9):
#         ch1=[0]*10
#         ch2=[0]*10
#         for j in range(9):
#             ch1[a[i][j]]=1
#             ch2[a[j][i]]=1
#         if sum(ch1)!=9 or sum(ch2)!=9:
#             return False
#     for i in range(3):
#         for j in range(3):
#             ch3=[0]*10
#             for k in range(3):
#                 for s in range(3):
#                     ch3[a[i*3+k][j*3+s]]=1
#             if sum(ch3)!=9:
#                 return False
#     return True

# a=[list(map(int, input().split())) for _ in range(9)]
# if check(a):
#     print("YES")
# else:
#     print("NO")