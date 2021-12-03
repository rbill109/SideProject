import sys
n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
left = 0
right = n-1
while left <= right:
    mid_idx = (left+right)//2
    mid = a[mid_idx]
    if m == mid:
        print(mid_idx+1)
        break
    elif m < mid:
        right = mid_idx - 1
    else:
        left = mid_idx + 1


# def BinarySearch(array, target, left, right):
#     mid_idx = (left+right)//2
#     mid = array[mid_idx]
#     if target == mid:
#         print(mid_idx+1)
#     elif target < median:
#         BinarySearch(array, target, left, mid_idx-1)
#     else:
#         BinarySearch(array, target, mid_idx+1, right)


# import sys
# n, m = map(int, sys.stdin.readline().split())
# a = list(map(int, sys.stdin.readline().split()))
# a.sort()
# BinarySearch(a, m, 0, n-1) 