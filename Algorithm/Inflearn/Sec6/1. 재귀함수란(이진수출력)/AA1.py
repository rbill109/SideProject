import sys

def Binary_scale(num):
    # case 1
    if num == 0:
        return
    else:
        Binary_scale(num//2)
        print(num%2,end="")
    
    # # case 2
    # if num > 0:
    #     Binary_scale(num//2)
    #     print(num%2,end="")

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    Binary_scale(n)