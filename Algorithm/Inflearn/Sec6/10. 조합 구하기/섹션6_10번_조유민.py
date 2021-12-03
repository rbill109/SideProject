#!/usr/bin/env python
"""
Created on Thu Feb 4 2021

@author: yumin cho
"""
import sys

def DFS(v, s):
    global cnt
    if v==m:
        for i in a:
            print(i, end=' ')
        print()
        cnt += 1
    else:
        for i in range(s, n+1): 
            a[v]=i
            DFS(v+1, i+1)


if __name__=="__main__":
    n, m = map(int, sys.stdin.readline().split())
    a = [0]*m
    cnt=0
    check = [0]*(n+1)
    DFS(0, 1)
    print(cnt)