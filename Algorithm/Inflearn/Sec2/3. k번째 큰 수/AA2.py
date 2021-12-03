import sys
from itertools import combinations

N, K = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

case = list(set([sum(i) for i in combinations(card, 3)]))
case.sort()
print(case[-K])