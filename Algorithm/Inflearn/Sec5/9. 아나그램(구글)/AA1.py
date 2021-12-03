#!/usr/bin/env python
"""
Created on Fri Jan 29 2021

@author: yumin cho
"""

import sys
from collections import Counter
word1 = Counter(sys.stdin.readline().strip())
word2 = Counter(sys.stdin.readline().strip())
if word1 == word2:
    print("YES")
else:
    print("NO")
